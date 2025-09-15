"""MirMir Research Agent - Integrated into Deep Research System.

This is a complete copy of the MirMir Agent with EXACT prompts and tool descriptions
that cost millions of USD to develop. DO NOT MODIFY the system prompt or tool descriptions.
"""

import os
import sys
import json
import glob as glob_module
import subprocess
import uuid
from pathlib import Path
from typing import List, Dict, Any, Optional
from langchain_xai import ChatXAI
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_core.tools import BaseTool, tool


# ================================================================================
# EXACT TOOL IMPLEMENTATIONS WITH EXACT DESCRIPTIONS
# ================================================================================

# Global storage for background processes
BACKGROUND_PROCESSES = {}


@tool("Read")
def read_file(
    file_path: str,
    offset: Optional[int] = None,
    limit: Optional[int] = None,
) -> str:
    """Reads a file from the local filesystem. You can access any file directly by using this tool.
    Assume this tool is able to read all files on the machine. If the User provides a path to a file assume that path is valid.
    It is okay to read a file that does not exist; an error will be returned.

    Usage:
    - The file_path parameter must be an absolute path, not a relative path
    - By default, it reads up to 2000 lines starting from the beginning of the file
    - You can optionally specify a line offset and limit (especially handy for long files)
    - Any lines longer than 2000 characters will be truncated
    - Results are returned using cat -n format, with line numbers starting at 1
    - This tool allows reading images (eg PNG, JPG, etc). When reading an image file the contents are presented visually
    - This tool can read PDF files (.pdf). PDFs are processed page by page, extracting both text and visual content
    - This tool can read Jupyter notebooks (.ipynb files) and returns all cells with their outputs
    - You have the capability to call multiple tools in a single response. It is always better to speculatively read multiple files as a batch

    Args:
        file_path: The absolute path to the file to read
        offset: The line number to start reading from. Only provide if the file is too large to read at once
        limit: The number of lines to read. Only provide if the file is too large to read at once

    Returns:
        The contents of the file with line numbers, or an error message if the file cannot be read
    """
    try:
        file_path = os.path.abspath(file_path)

        if not os.path.exists(file_path):
            return f"Error: File not found: {file_path}"

        if os.path.isdir(file_path):
            return f"Error: Path is a directory, not a file: {file_path}"

        # For binary files (images, PDFs)
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.pdf')):
            return f"[Binary file: {file_path} - Content preview not available in text format]"

        # For Jupyter notebooks
        if file_path.lower().endswith('.ipynb'):
            with open(file_path, 'r', encoding='utf-8') as f:
                notebook = json.load(f)
                output = []
                for i, cell in enumerate(notebook.get('cells', []), 1):
                    cell_type = cell.get('cell_type', 'unknown')
                    source = ''.join(cell.get('source', []))
                    output.append(f"Cell {i} [{cell_type}]:\n{source}\n")
                return '\n'.join(output)

        # Regular text files
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        start_line = (offset - 1) if offset else 0
        end_line = start_line + (limit if limit else 2000)

        result_lines = []
        for i, line in enumerate(lines[start_line:end_line], start=start_line + 1):
            line = line.rstrip('\n')
            if len(line) > 2000:
                line = line[:2000] + '... [truncated]'
            result_lines.append(f"{i:6}\t{line}")

        if not result_lines:
            return "[File is empty]"

        return '\n'.join(result_lines)

    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool("Write")
def write_file(file_path: str, content: str) -> str:
    """Writes a file to the local filesystem.

    Usage:
    - This tool will overwrite the existing file if there is one at the provided path
    - If this is an existing file, you MUST use the Read tool first to read the file's contents
    - ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required
    - NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested

    Args:
        file_path: The absolute path to the file to write (must be absolute, not relative)
        content: The content to write to the file

    Returns:
        Success message or error message
    """
    try:
        file_path = os.path.abspath(file_path)

        # Create parent directory if it doesn't exist
        parent_dir = os.path.dirname(file_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return f"Successfully wrote to {file_path}"

    except Exception as e:
        return f"Error writing file: {str(e)}"


@tool("LS")
def list_files(directory: str = ".") -> str:
    """List files and directories with detailed information.

    Lists contents of a directory with permissions, size, and modification time in a format similar to 'ls -la'.
    Hidden files (starting with .) are included in the output.

    Args:
        directory: The directory to list (defaults to current directory)

    Returns:
        Directory listing in ls -la format, or error message
    """
    try:
        directory = os.path.abspath(directory)

        if not os.path.exists(directory):
            return f"Error: Directory not found: {directory}"

        if not os.path.isdir(directory):
            return f"Error: Not a directory: {directory}"

        # Use actual ls command for better output
        result = subprocess.run(
            ["ls", "-la", directory],
            capture_output=True,
            text=True,
            cwd=directory
        )

        if result.returncode != 0:
            return f"Error listing directory: {result.stderr}"

        return result.stdout

    except Exception as e:
        return f"Error: {str(e)}"


@tool("Bash")
def run_command(
    command: str,
    run_in_background: Optional[bool] = False,
    timeout: Optional[int] = 120000,
) -> str:
    """Executes a given bash command in a persistent shell session with optional timeout.

    Before executing the command, please follow these steps:

    1. Directory Verification:
       - If the command will create new directories or files, first use `ls` to verify the parent directory exists

    2. Command Execution:
       - Always quote file paths that contain spaces with double quotes
       - After ensuring proper quoting, execute the command
       - Capture the output of the command

    Usage notes:
      - The command argument is required
      - You can specify an optional timeout in milliseconds (up to 600000ms / 10 minutes)
      - If the output exceeds 30000 characters, output will be truncated
      - You can use the run_in_background parameter to run the command in the background
      - VERY IMPORTANT: You MUST avoid using search commands like `find` and `grep`. Use Grep or Glob tools instead
      - ALWAYS USE ripgrep at `rg` first if you need grep functionality
      - When issuing multiple commands, use ';' or '&&' to separate them

    Args:
        command: The command to execute
        run_in_background: Set to true to run this command in the background
        timeout: Optional timeout in milliseconds (max 600000)

    Returns:
        Command output or process ID if running in background
    """
    try:
        # Convert timeout from milliseconds to seconds
        timeout_seconds = min(timeout / 1000, 600) if timeout else 120

        if run_in_background:
            # Start process in background
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=os.getcwd()
            )

            # Generate a unique ID for this process
            process_id = str(uuid.uuid4())[:8]
            BACKGROUND_PROCESSES[process_id] = {
                'process': process,
                'command': command,
                'output': []
            }

            return f"Started background process with ID: {process_id}\nUse BashOutput tool with bash_id='{process_id}' to check output"
        else:
            # Run command and wait for completion
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                cwd=os.getcwd()
            )

            output = result.stdout + result.stderr

            # Truncate if too long
            if len(output) > 30000:
                output = output[:30000] + "\n... [Output truncated]"

            return output if output else "[Command completed with no output]"

    except subprocess.TimeoutExpired:
        return f"Error: Command timed out after {timeout_seconds} seconds"
    except Exception as e:
        return f"Error executing command: {str(e)}"


@tool("BashOutput")
def get_bash_output(
    bash_id: str,
    filter: Optional[str] = None
) -> str:
    """Retrieves output from a running or completed background bash shell.

    - Takes a shell_id parameter identifying the shell
    - Always returns only new output since the last check
    - Returns stdout and stderr output along with shell status
    - Supports optional regex filtering to show only lines matching a pattern

    Args:
        bash_id: The ID of the background shell to retrieve output from
        filter: Optional regular expression to filter the output lines

    Returns:
        New output from the background process
    """
    try:
        if bash_id not in BACKGROUND_PROCESSES:
            return f"Error: No background process found with ID: {bash_id}"

        proc_info = BACKGROUND_PROCESSES[bash_id]
        process = proc_info['process']

        # Check if process is still running
        poll = process.poll()
        is_running = poll is None

        # Read any new output
        new_output = []
        if process.stdout:
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                if filter:
                    import re
                    if re.search(filter, line):
                        new_output.append(line.rstrip())
                else:
                    new_output.append(line.rstrip())

        # Store output
        proc_info['output'].extend(new_output)

        # Prepare response
        status = "running" if is_running else f"completed (exit code: {poll})"
        output_text = '\n'.join(new_output) if new_output else "[No new output]"

        return f"Process status: {status}\nOutput:\n{output_text}"

    except Exception as e:
        return f"Error retrieving output: {str(e)}"


@tool("Glob")
def glob_files(pattern: str, path: Optional[str] = None) -> str:
    """Fast file pattern matching tool that works with any codebase size.

    - Supports glob patterns like "**/*.js" or "src/**/*.ts"
    - Returns matching file paths sorted by modification time
    - Use this tool when you need to find files by name patterns
    - You have the capability to call multiple tools in a single response

    Args:
        pattern: The glob pattern to match files against
        path: The directory to search in. If not specified, the current working directory will be used

    Returns:
        List of matching file paths, one per line
    """
    try:
        if path:
            search_path = os.path.abspath(path)
        else:
            search_path = os.getcwd()

        if not os.path.exists(search_path):
            return f"Error: Path not found: {search_path}"

        # Combine path with pattern if path is provided
        if path:
            full_pattern = os.path.join(search_path, pattern)
        else:
            full_pattern = pattern

        # Find matching files
        matches = glob_module.glob(full_pattern, recursive=True)

        if not matches:
            return f"No files matching pattern: {pattern}"

        # Sort by modification time (newest first)
        matches.sort(key=lambda x: os.path.getmtime(x) if os.path.exists(x) else 0, reverse=True)

        # Return one file per line
        return '\n'.join(matches)

    except Exception as e:
        return f"Error: {str(e)}"


@tool("Grep")
def grep_files(
    pattern: str,
    path: Optional[str] = None,
    glob: Optional[str] = None,
    output_mode: Optional[str] = "files_with_matches",
    case_insensitive: Optional[bool] = False,
    show_line_numbers: Optional[bool] = False,
    context_lines: Optional[int] = None,
    head_limit: Optional[int] = None,
) -> str:
    """A powerful search tool built on ripgrep

    Usage:
    - ALWAYS use Grep for search tasks. NEVER invoke `grep` or `rg` as a Bash command
    - Supports full regex syntax (e.g., "log.*Error", "function\\s+\\w+")
    - Filter files with glob parameter (e.g., "*.js", "**/*.tsx")
    - Output modes: "content" shows matching lines, "files_with_matches" shows only file paths (default), "count" shows match counts
    - Pattern syntax: Uses ripgrep (not grep) - literal braces need escaping

    Args:
        pattern: The regular expression pattern to search for in file contents
        path: File or directory to search in (defaults to current working directory)
        glob: Glob pattern to filter files (e.g. "*.js", "*.{ts,tsx}")
        output_mode: Output mode - "content", "files_with_matches", or "count" (default: "files_with_matches")
        case_insensitive: Case insensitive search (default: False)
        show_line_numbers: Show line numbers in output (only for "content" mode)
        context_lines: Number of lines to show before and after each match (only for "content" mode)
        head_limit: Limit output to first N lines/entries

    Returns:
        Search results based on output mode
    """
    try:
        # Build ripgrep command
        cmd = ["rg"]

        # Add pattern
        cmd.append(pattern)

        # Add path if specified
        if path:
            cmd.append(os.path.abspath(path))

        # Add options based on parameters
        if case_insensitive:
            cmd.append("-i")

        if glob:
            cmd.extend(["--glob", glob])

        # Handle output mode
        if output_mode == "files_with_matches":
            cmd.append("-l")
        elif output_mode == "count":
            cmd.append("-c")
        elif output_mode == "content":
            if show_line_numbers:
                cmd.append("-n")
            if context_lines:
                cmd.extend(["-C", str(context_lines)])

        # Execute ripgrep
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if head_limit and output:
                lines = output.split('\n')
                output = '\n'.join(lines[:head_limit])
            return output if output else "No matches found"
        elif result.returncode == 1:
            return "No matches found"
        else:
            # Check if ripgrep is installed
            check_rg = subprocess.run(["which", "rg"], capture_output=True)
            if check_rg.returncode != 0:
                return "Error: ripgrep (rg) is not installed. Please install it first: brew install ripgrep"
            return f"Error running grep: {result.stderr}"

    except FileNotFoundError:
        return "Error: ripgrep (rg) is not installed. Please install it first: brew install ripgrep"
    except Exception as e:
        return f"Error: {str(e)}"


@tool("TodoWrite")
def todo_write(todos: List[Dict[str, str]]) -> str:
    """Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
    It also helps the user understand the progress of the task and overall progress of their requests.

    ## When to Use This Tool
    Use this tool proactively in these scenarios:

    1. Complex multi-step tasks - When a task requires 3 or more distinct steps or actions
    2. Non-trivial and complex tasks - Tasks that require careful planning or multiple operations
    3. User explicitly requests todo list - When the user directly asks you to use the todo list
    4. User provides multiple tasks - When users provide a list of things to be done (numbered or comma-separated)
    5. After receiving new instructions - Immediately capture user requirements as todos
    6. When you start working on a task - Mark it as in_progress BEFORE beginning work. Ideally you should only have one todo as in_progress at a time
    7. After completing a task - Mark it as completed and add any new follow-up tasks discovered during implementation

    ## When NOT to Use This Tool

    Skip using this tool when:
    1. There is only a single, straightforward task
    2. The task is trivial and tracking it provides no organizational benefit
    3. The task can be completed in less than 3 trivial steps
    4. The task is purely conversational or informational

    NOTE that you should not use this tool if there is only one trivial task to do. In this case you are better off just doing the task directly.

    ## Examples of When to Use the Todo List

    <example>
    User: I want to add a dark mode toggle to the application settings. Make sure you run the tests and build when you're done!
    Assistant: I'll help add a dark mode toggle to your application settings. Let me create a todo list to track this implementation.
    *Creates todo list with the following items:*
    1. Creating dark mode toggle component in Settings page
    2. Adding dark mode state management (context/store)
    3. Implementing CSS-in-JS styles for dark theme
    4. Updating existing components to support theme switching
    5. Running tests and build process, addressing any failures or errors that occur
    *Begins working on the first task*

    <reasoning>
    The assistant used the todo list because:
    1. Adding dark mode is a multi-step feature requiring UI, state management, and styling changes
    2. The user explicitly requested tests and build be run afterward
    3. The assistant inferred that tests and build need to pass by adding "Ensure tests and build succeed" as the final task
    </reasoning>
    </example>

    <example>
    User: Help me rename the function getCwd to getCurrentWorkingDirectory across my project
    Assistant: Let me first search through your codebase to find all occurrences of 'getCwd'.
    *Uses grep or search tools to locate all instances of getCwd in the codebase*
    Assistant: I've found 15 instances of 'getCwd' across 8 different files. Let me create a todo list to track these changes.
    *Creates todo list with specific items for each file that needs updating*

    <reasoning>
    The assistant used the todo list because:
    1. First, the assistant searched to understand the scope of the task
    2. Upon finding multiple occurrences across different files, it determined this was a complex task with multiple steps
    3. The todo list helps ensure every instance is tracked and updated systematically
    4. This approach prevents missing any occurrences and maintains code consistency
    </reasoning>
    </example>


    <example>
    User: I need to implement these features for my e-commerce site: user registration, product catalog, shopping cart, and checkout flow.
    Assistant: I'll help implement these features. First, let's add all the features to the todo list.
    *Creates a todo list breaking down each feature into specific tasks based on the project architecture*
    Assistant: Let's start with user registration. This will involve creating database models, API endpoints, and frontend forms that integrate with your existing authentication system.

    <reasoning>
    The assistant used the todo list because:
    1. The user provided multiple complex features to implement in a comma separated list
    2. The todo list helps organize these large features into manageable tasks
    3. This approach allows for tracking progress across the entire implementation
    </reasoning>
    </example>

    <example>
    User: Can you help optimize my React application? It's rendering slowly and has performance issues.</user>
    Assistant: I'll help optimize your React application. First, let me examine your codebase to identify potential performance bottlenecks.
    *Reviews component structure, render patterns, state management, and data fetching*
    Assistant: After analyzing your codebase, I've identified several performance issues. Let me create a todo list to track our optimization efforts.
    *Creates todo list with items like: 1) Implementing memoization for expensive calculations in ProductList, 2) Adding virtualization for long lists in Dashboard, 3) Optimizing image loading in Gallery component, 4) Fixing state update loops in ShoppingCart, 5) Reviewing bundle size and implementing code splitting*
    Let's start by implementing memoization for the expensive calculations in your ProductList component.</assistant>

    <reasoning>
    The assistant used the todo list because:
    1. First, the assistant examined the codebase to identify specific performance issues
    2. Based on this analysis, it identified multiple optimization opportunities
    3. Performance optimization is a non-trivial task requiring multiple steps
    4. The todo list helps methodically track improvements across different components
    5. This systematic approach ensures all performance bottlenecks are addressed
    </reasoning>
    </example>

    ## Examples of When NOT to Use the Todo List

    <example>
    User: How do I print 'Hello World' in Python?
    Assistant: In Python, you can print "Hello World" with this simple code:

    python
    print("Hello World")

    This will output the text "Hello World" to the console when executed.</assistant>

    <reasoning>
    The assistant did not use the todo list because this is a single, trivial task that can be completed in one step. There's no need to track multiple tasks or steps for such a straightforward request.
    </reasoning>
    </example>

    <example>
    User: What does the git status command do?
    Assistant: The git status command shows the current state of your working directory and staging area. It displays which changes have been staged, which haven't, and which files aren't being tracked by Git. This is a fundamental command for understanding the current state of your repository before making commits.

    <reasoning>
    The assistant did not use the todo list because this is an informational request with no actual coding task to complete. The user is simply asking for an explanation, not for the assistant to perform multiple steps or tasks.
    </reasoning>
    </example>

    <example>
    User: Can you add a comment to the calculateTotal function to explain what it does?
    Assistant: Sure, let me add a comment to the calculateTotal function to explain what it does.
    * Uses the Edit tool to add a comment to the calculateTotal function *

    <reasoning>
    The assistant did not use the todo list because this is a single, straightforward task confined to one location in the code. Adding a comment doesn't require tracking multiple steps or systematic organization.
    </reasoning>
    </example>

    <example>
    User: Run npm install for me and tell me what happens.
    Assistant: I'll run the npm install command for you.

    *Executes: npm install*

    The command completed successfully. Here's the output:
    [Output of npm install command]

    All dependencies have been installed according to your package.json file.

    <reasoning>
    The assistant did not use the todo list because this is a single command execution with immediate results. There are no multiple steps to track or organize, making the todo list unnecessary for this straightforward task.
    </reasoning>
    </example>

    ## Task States and Management

    1. **Task States**: Use these states to track progress:
       - pending: Task not yet started
       - in_progress: Currently working on (limit to ONE task at a time)
       - completed: Task finished successfully

       **IMPORTANT**: Task descriptions must have two forms:
       - content: The imperative form describing what needs to be done (e.g., "Run tests", "Build the project")
       - activeForm: The present continuous form shown during execution (e.g., "Running tests", "Building the project")

    2. **Task Management**:
       - Update task status in real-time as you work
       - Mark tasks complete IMMEDIATELY after finishing (don't batch completions)
       - Exactly ONE task must be in_progress at any time (not less, not more)
       - Complete current tasks before starting new ones
       - Remove tasks that are no longer relevant from the list entirely

    3. **Task Completion Requirements**:
       - ONLY mark a task as completed when you have FULLY accomplished it
       - If you encounter errors, blockers, or cannot finish, keep the task as in_progress
       - When blocked, create a new task describing what needs to be resolved
       - Never mark a task as completed if:
         - Tests are failing
         - Implementation is partial
         - You encountered unresolved errors
         - You couldn't find necessary files or dependencies

    4. **Task Breakdown**:
       - Create specific, actionable items
       - Break complex tasks into smaller, manageable steps
       - Use clear, descriptive task names
       - Always provide both forms:
         - content: "Fix authentication bug"
         - activeForm: "Fixing authentication bug"

    When in doubt, use this tool. Being proactive with task management demonstrates attentiveness and ensures you complete all requirements successfully.

    Args:
        todos: List of todo items, each with 'content', 'status', and 'activeForm' keys

    Returns:
        Confirmation message
    """
    # Validation
    try:
        for todo in todos:
            if not all(key in todo for key in ['content', 'status', 'activeForm']):
                return "Error: Each todo must have 'content', 'status', and 'activeForm' keys"

            if todo['status'] not in ['pending', 'in_progress', 'completed']:
                return f"Error: Invalid status '{todo['status']}'. Must be pending/in_progress/completed"

        # Count in_progress tasks
        in_progress = sum(1 for t in todos if t['status'] == 'in_progress')
        if in_progress > 1:
            return "Error: Only one task can be in_progress at a time"

        # Check for partial lists
        completed_count = sum(1 for t in todos if t['status'] == 'completed')
        if completed_count > 0 and len(todos) < 3:
            return (
                "⚠️ WARNING: Partial todo list detected! You sent only {} items but have {} completed tasks.\n"
                "Please resend with the COMPLETE todo list including ALL tasks:\n"
                "- All pending tasks\n"
                "- All in_progress tasks (usually 1)\n"
                "- All completed tasks\n"
                "This ensures full context is maintained."
            ).format(len(todos), completed_count)

        # Save todos to file for persistence (optional)
        todos_file = os.path.join(os.getcwd(), '.mirmir_todos.json')
        with open(todos_file, 'w') as f:
            json.dump(todos, f, indent=2)

        return "Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable"

    except Exception as e:
        return f"Error updating todos: {str(e)}"


# ================================================================================
# MIRMIR RESEARCH AGENT CLASS
# ================================================================================

class MirMirResearchAgent:
    """MirMir agent for querying MoMo business data - EXACT implementation."""

    def __init__(self):
        """Initialize the MirMir agent with EXACT configuration."""
        # Initialize LLM with Grok - EXACT configuration
        xai_api_key = os.getenv("XAI_API_KEY")
        if not xai_api_key:
            raise ValueError("XAI_API_KEY environment variable is required")

        self.llm = ChatXAI(
            model="grok-code-fast-1",
            api_key=xai_api_key,
            temperature=0,
            max_tokens=16384,
        )

        # Setup tools - EXACTLY as in original
        self.tools = self._get_tools()
        self.tools_map = {tool.name: tool for tool in self.tools}
        self.llm_with_tools = self.llm.bind_tools(self.tools)

        # Load memory
        self.memory_context = self._load_mirmir_memory()

        # Initialize with EXACT system prompt
        self.messages = [SystemMessage(content=self._get_system_prompt())]

        # Add memory as second message (like sonph-code does)
        if self.memory_context:
            self.messages.append(HumanMessage(content=self.memory_context))

    def _get_system_prompt(self) -> str:
        """Get the EXACT system prompt from MirMir Agent - DO NOT MODIFY."""
        import platform
        from datetime import datetime

        today = datetime.now().strftime("%Y-%m-%d")
        os_info = f"{platform.system()} {platform.release()}"
        current_working_dir = os.path.abspath(os.getcwd())

        # This is the EXACT prompt from sonph-code with minimal MirMir-specific additions
        return f"""
You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user.

IMPORTANT: Assist with defensive security tasks only. Refuse to create, modify, or improve code that may be used maliciously. Allow security analysis, detection rules, vulnerability explanations, defensive tools, and security documentation.
IMPORTANT: You must NEVER generate or guess URLs for the user unless you are confident that the URLs are for helping the user with programming. You may use URLs provided by the user in their messages or local files.

If the user asks for help or wants to give feedback inform them of the following:
- /help: Get help with using Claude Code
- To give feedback, users should report the issue at https://github.com/anthropics/claude-code/issues

# MirMir-Specific Context
You are specialized in querying MoMo business data through MirMir API. You have access to:
- MirMir API documentation (search for mir_mir_apis.md if not found in docs/api_docs/)
- MirMir overview (search for mirmir_overview.md if not found in docs/)
- 43 domain documentation files (search for mirmir_domains/ directory or final_*.md pattern)

MirMir queries must include: data type, time range, and "KHÔNG cần chart"

IMPORTANT: If any documentation files are not found in expected locations:
1. Use Glob tool to search for them (e.g., "**/mirmir_overview.md", "**/final_*.md")
2. Update your references to the new locations
3. Continue with the task using the found files

# Tone and style
You should be concise, direct, and to the point.
You MUST answer concisely with fewer than 4 lines (not including tool use or code generation), unless user asks for detail.
IMPORTANT: You should minimize output tokens as much as possible while maintaining helpfulness, quality, and accuracy. Only address the specific query or task at hand, avoiding tangential information unless absolutely critical for completing the request. If you can answer in 1-3 sentences or a short paragraph, please do.
IMPORTANT: You should NOT answer with unnecessary preamble or postamble (such as explaining your code or summarizing your action), unless the user asks you to.
Do not add additional code explanation summary unless requested by the user. After working on a file, just stop, rather than providing an explanation of what you did.
Answer the user's question directly, without elaboration, explanation, or details. One word answers are best. Avoid introductions, conclusions, and explanations. You MUST avoid text before/after your response, such as "The answer is <answer>.", "Here is the content of the file..." or "Based on the information provided, the answer is..." or "Here is what I will do next...". Here are some examples to demonstrate appropriate verbosity:
<example>
user: 2 + 2
assistant: 4
</example>

<example>
user: what is 2+2?
assistant: 4
</example>

<example>
user: is 11 a prime number?
assistant: Yes
</example>

<example>
user: what command should I run to list files in the current directory?
assistant: ls
</example>

<example>
user: what command should I run to watch files in the current directory?
assistant: [runs ls to list the files in the current directory, then read docs/commands in the relevant file to find out how to watch files]
npm run dev
</example>

<example>
user: How many golf balls fit inside a jetta?
assistant: 150000
</example>

<example>
user: what files are in the directory src/?
assistant: [runs ls and sees foo.c, bar.c, baz.c]
user: which file contains the implementation of foo?
assistant: src/foo.c
</example>
When you run a non-trivial bash command, you should explain what the command does and why you are running it, to make sure the user understands what you are doing (this is especially important when you are running a command that will make changes to the user's system).
Remember that your output will be displayed on a command line interface. Your responses can use Github-flavored markdown for formatting, and will be rendered in a monospace font using the CommonMark specification.
Output text to communicate with the user; all text you output outside of tool use is displayed to the user. Only use tools to complete tasks. Never use tools like Bash or code comments as means to communicate with the user during the session.
If you cannot or will not help the user with something, please do not say why or what it could lead to, since this comes across as preachy and annoying. Please offer helpful alternatives if possible, and otherwise keep your response to 1-2 sentences.
Only use emojis if the user explicitly requests it. Avoid using emojis in all communication unless asked.
IMPORTANT: Keep your responses short, since they will be displayed on a command line interface.

# Proactiveness
You are allowed to be proactive, but only when the user asks you to do something. You should strive to strike a balance between:
- Doing the right thing when asked, including taking actions and follow-up actions
- Not surprising the user with actions you take without asking
For example, if the user asks you how to approach something, you should do your best to answer their question first, and not immediately jump into taking actions.

# Following conventions
When making changes to files, first understand the file's code conventions. Mimic code style, use existing libraries and utilities, and follow existing patterns.
- NEVER assume that a given library is available, even if it is well known. Whenever you write code that uses a library or framework, first check that this codebase already uses the given library. For example, you might look at neighboring files, or check the package.json (or cargo.toml, and so on depending on the language).
- When you create a new component, first look at existing components to see how they're written; then consider framework choice, naming conventions, typing, and other conventions.
- When you edit a piece of code, first look at the code's surrounding context (especially its imports) to understand the code's choice of frameworks and libraries. Then consider how to make the given change in a way that is most idiomatic.
- Always follow security best practices. Never introduce code that exposes or logs secrets and keys. Never commit secrets or keys to the repository.

# Code style
- IMPORTANT: DO NOT ADD ***ANY*** COMMENTS unless asked


# Task Management
You have access to the TodoWrite tools to help you manage and plan tasks. Use these tools VERY frequently to ensure that you are tracking your tasks and giving the user visibility into your progress.
These tools are also EXTREMELY helpful for planning tasks, and for breaking down larger complex tasks into smaller steps. If you do not use this tool when planning, you may forget to do important tasks - and that is unacceptable.

CRITICAL: Every TodoWrite call MUST include the COMPLETE todo list - ALL pending, in_progress, and completed tasks. Never send partial updates with only 1-2 items. This maintains full context across the conversation.

It is critical that you mark todos as completed as soon as you are done with a task. Do not batch up multiple tasks before marking them as completed.

Examples:

<example>
user: Run the build and fix any type errors
assistant: I'm going to use the TodoWrite tool to write the following items to the todo list:
- Run the build
- Fix any type errors

I'm now going to run the build using Bash.

Looks like I found 10 type errors. I'm going to use the TodoWrite tool to write 10 items to the todo list.

marking the first todo as in_progress

Let me start working on the first item...

The first item has been fixed, let me mark the first todo as completed, and move on to the second item...
..
..
</example>
In the above example, the assistant completes all the tasks, including the 10 error fixes and running the build and fixing all errors.

<example>
user: Help me write a new feature that allows users to track their usage metrics and export them to various formats

assistant: I'll help you implement a usage metrics tracking and export feature. Let me first use the TodoWrite tool to plan this task.
Adding the following todos to the todo list:
1. Research existing metrics tracking in the codebase
2. Design the metrics collection system
3. Implement core metrics tracking functionality
4. Create export functionality for different formats

Let me start by researching the existing codebase to understand what metrics we might already be tracking and how we can build on that.

I'm going to search for any existing metrics or telemetry code in the project.

I've found some existing telemetry code. Let me mark the first todo as in_progress and start designing our metrics tracking system based on what I've learned...

[Assistant continues implementing the feature step by step, marking todos as in_progress and completed as they go]
</example>


Users may configure 'hooks', shell commands that execute in response to events like tool calls, in settings. Treat feedback from hooks, including <user-prompt-submit-hook>, as coming from the user. If you get blocked by a hook, determine if you can adjust your actions in response to the blocked message. If not, ask the user to check their hooks configuration.

# Doing tasks
The user will primarily request you perform software engineering tasks. This includes solving bugs, adding new functionality, refactoring code, explaining code, and more. For these tasks the following steps are recommended:
- Use the TodoWrite tool to plan the task if required
- Use the available search tools to understand the codebase and the user's query. You are encouraged to use the search tools extensively both in parallel and sequentially.
- Implement the solution using all tools available to you
- Verify the solution if possible with tests. NEVER assume specific test framework or test script. Check the README or search codebase to determine the testing approach.
- VERY IMPORTANT: When you have completed a task, you MUST run the lint and typecheck commands (eg. npm run lint, npm run typecheck, ruff, etc.) with Bash if they were provided to you to ensure your code is correct. If you are unable to find the correct command, ask the user for the command to run and if they supply it, proactively suggest writing it to CLAUDE.md so that you will know to run it next time.
NEVER commit changes unless the user explicitly asks you to. It is VERY IMPORTANT to only commit when explicitly asked, otherwise the user will feel that you are being too proactive.

- Tool results and user messages may include <system-reminder> tags. <system-reminder> tags contain useful information and reminders. They are NOT part of the user's provided input or the tool result.



# Tool usage policy
- When doing file search, prefer to use the Task tool in order to reduce context usage.
- You should proactively use the Task tool with specialized agents when the task at hand matches the agent's description.
- You have the capability to call multiple tools in a single response. When multiple independent pieces of information are requested, batch your tool calls together for optimal performance. When making multiple bash tool calls, you MUST send a single message with multiple tools calls to run the calls in parallel. For example, if you need to run "git status" and "git diff", send a single message with two tool calls to run the calls in parallel.


Here is useful information about the environment you are running in:
<env>
Working directory: {current_working_dir}
Is directory a git repo: No
Platform: {os_info}
OS Version: {platform.system()} {platform.release()}
Today's date: {today}
</env>

Assistant knowledge cutoff is January 2025.

IMPORTANT: Assist with defensive security tasks only. Refuse to create, modify, or improve code that may be used maliciously. Allow security analysis, detection rules, vulnerability explanations, defensive tools, and security documentation.

IMPORTANT: Always use the TodoWrite tool to plan and track tasks throughout the conversation.

# Code References

When referencing specific functions or pieces of code include the pattern  to allow the user to easily navigate to the source code location.

<example>
user: Where are errors from the client handled?
assistant: Clients are marked as failed in the  function in src/services/process.ts:712.
</example>

Remember: Be direct, efficient, and respect the user's existing codebase conventions."""

    def _get_tools(self) -> List[BaseTool]:
        """Get the tools for MirMir agent - EXACTLY as in original."""
        return [
            read_file,
            write_file,
            run_command,
            get_bash_output,
            list_files,
            glob_files,
            grep_files,
            todo_write,
        ]

    def _load_mirmir_memory(self) -> str:
        """Load MirMir memory with EXACT format from original."""
        # Look for memory files in mirmir_memory directory
        base_path = Path(__file__).parent / "mirmir_memory"
        overview_path = base_path / "mirmir_overview.md"

        # If mirmir_memory doesn't exist, try sample_codes location
        if not overview_path.exists():
            alt_base = Path(__file__).parent / "sample_codes" / "auto-explore" / "docs"
            alt_overview = alt_base / "mirmir_overview.md"
            if alt_overview.exists():
                overview_path = alt_overview
                base_path = alt_base.parent

        if overview_path.exists():
            with open(overview_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find domains directory
            domains_path = base_path / "data" / "mirmir_domains"
            if not domains_path.exists():
                domains_path = base_path / "mirmir_domains"

            # File location note
            file_location_note = ""
            if domains_path.exists():
                file_location_note = f"""

## Important File Locations
- MirMir domains are located at: {domains_path}
- If files have been moved, use Glob or Grep tools to search for them
- Domain files follow pattern: final_*.md
"""

            # EXACT system-reminder format
            return f"""<system-reminder>
As you answer the user's questions, you can use the following context:
# MirMir Knowledge Base
{content}
{file_location_note}
IMPORTANT:
1. This context is your core knowledge about MirMir and MoMo data. Use it to answer questions accurately.
2. If referenced files are not found in expected locations, search for them using LS, Glob or Grep tools.
3. The mirmir_domains folder contains all domain documentation files (final_*.md pattern).
</system-reminder>"""

        # Fallback if no overview found
        return """<system-reminder>
# MirMir Knowledge Base
MirMir overview file not found in expected location.

## File Search Instructions
- Use Glob tool to search for "mirmir_overview.md" and "mirmir_domains" directory
- Domain files follow pattern: final_*.md
- Common locations: docs/, data/, or project root
- If files moved, search and update paths accordingly

IMPORTANT: Always search for files if not found in expected locations.
</system-reminder>"""

    def query_momo_data(self, query: str) -> str:
        """Process MoMo data query using EXACT chat loop from MirMir Agent."""
        # Reset messages for new query (keep system prompt and memory)
        self.messages = [self.messages[0]]  # Keep system prompt
        if len(self.messages) > 1 and "MirMir Knowledge Base" in self.messages[1].content:
            self.messages.append(self.messages[1])  # Keep memory context

        # Add user message
        self.messages.append(HumanMessage(content=query))

        try:
            # Get initial response from LLM
            response = self.llm_with_tools.invoke(self.messages)
            self.messages.append(response)

            # CRITICAL: Use WHILE loop to keep processing tool calls until none remain
            while hasattr(response, "tool_calls") and response.tool_calls:
                for tool_call in response.tool_calls:
                    tool_name = tool_call["name"]
                    tool_args = tool_call["args"]
                    tool = self.tools_map[tool_name]

                    try:
                        # Execute tool
                        result = tool.invoke(tool_args)

                        # Add tool result to messages
                        tool_msg = ToolMessage(
                            content=str(result),
                            tool_call_id=tool_call["id"],
                        )
                        self.messages.append(tool_msg)
                    except Exception as e:
                        # Add error message
                        tool_msg = ToolMessage(
                            content=f"Error: {str(e)}",
                            tool_call_id=tool_call["id"],
                        )
                        self.messages.append(tool_msg)

                # Get next response after tool execution
                response = self.llm_with_tools.invoke(self.messages)
                self.messages.append(response)

            # After all tool calls are processed, return the final content
            if response.content:
                return response.content
            else:
                return "Task completed successfully."

        except Exception as e:
            return f"Error processing MoMo data query: {str(e)}"