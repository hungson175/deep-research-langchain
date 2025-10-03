"""
Quick test script to generate insight HTML from a markdown report
"""
import asyncio
from src.core.insight_generator import generate_insight_from_notes

async def main():
    # Extract key findings from the report as "research notes"
    research_notes = [
        """
**Key Finding 1: Fraud Reduction**
- Biometric upgrades reduced fraud by 50-72% since July 2024
- Fraud-related accounts dropped 72% to 682 cases
- Money transfer incidents fell 50% to 700 cases
- Banking fraud causing customer losses fell 50% in August 2024
- By August 2025: 59% drop in individual fraud, 52% in illicit fund accounts

**Key Finding 2: Market Growth & AI Investment**
- Vietnam fintech market: $15.4B in 2025, growing 17.8% CAGR to 2034
- Regional mobile payments: $475B by 2027
- AI investment: $1.52B by 2030, contributing 12% to GDP
- Visa prevented $27B in fraud in 2022 using AI models
- AI can reduce costs by 7-9% and boost revenue 9% by 2027
        """,
        """
**Key Finding 3: Regulatory Compliance**
- Circular 17/2024: Mandatory biometric verification for corporate accounts (July 2025)
- 120.9M individual and 1.2M organizational records validated by August 2025
- 86M unverified accounts deactivated (43% of total)
- 57% compliance rate achieved
- Magnetic stripe ban effective July 2025, promoting EMV chip cards

**Key Finding 4: Urban vs Rural Gap**
- Urban: 91% adoption (Millennials/Gen Z), 97-98% digital transactions
- Rural (62% of population): Only 34% using mobile money
- 73.7% rural users seek financial literacy education
- Low-income: Only 47% banked vs 97% high-income
- Infrastructure gaps and low literacy create -0.9% market impact
        """,
        """
**Key Finding 5: Emerging Threats**
- APAC deepfake fraud surged 1500% in 2023
- $485.6B in fraud losses
- Vietnam: $39M laundered via spoofed biometrics (May 2025)
- Phishing emails rose 341% in six months
- AI-driven threats require continuous upgrades

**Implementation ROI for MoMo:**
- Expected fraud reduction: 40-50%
- Cost savings: 7-9% via AI automation
- Revenue growth: 9% by 2027
- User trust increase: +22%
- ROI: Up to 300% via efficiencies
        """
    ]

    research_brief = """
AI and Biometric Security in Fraud Prevention: Analyzing effectiveness of biometric
upgrades in reducing fraud, AI applications in risk assessment, compliance costs,
user adoption rates (urban vs rural), and emerging threats for MoMo in Vietnam's fintech market.
    """

    success, output_path = await generate_insight_from_notes(
        research_notes=research_notes,
        research_brief=research_brief,
        output_filename="test_short.html",
        output_dir="reports/htmls",
        title="AI & Biometric Security in Vietnam Fintech",
        quiet=False
    )

    if success:
        print(f"\n✅ Success! Generated: {output_path}")
    else:
        print(f"\n❌ Failed to generate insight page")

if __name__ == "__main__":
    asyncio.run(main())
