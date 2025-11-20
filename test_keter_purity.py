#!/usr/bin/env python3
"""
Quick test of Keter purity for Venezuela case
"""

import sys
sys.path.insert(0, '/home/user/tikun')

from test_venezuela_NEUTRAL import VENEZUELA_CASE_NEUTRAL
from keter_purification_system import KeterPurityValidator, generate_neutrality_report

def main():
    print("\n" + "="*80)
    print("TESTING KETER PURITY - VENEZUELA CASE")
    print("="*80 + "\n")

    validator = KeterPurityValidator()
    validation = validator.validate_case(VENEZUELA_CASE_NEUTRAL)

    print(f"✓ Purity Score: {validation['purity_score']:.1f}%")
    print(f"✓ Bias Score: {validation['bias_report']['bias_score']*100:.1f}%")
    print(f"✓ Bias Level: {validation['bias_report']['bias_level']}")
    print(f"✓ Status: {validation['certification']}\n")

    if validation['issues']:
        print(f"Issues found: {len(validation['issues'])}\n")
        for i, issue in enumerate(validation['issues'], 1):
            print(f"{i}. [{issue['severity'].upper()}] {issue['type']}")
            print(f"   {issue['description']}")
            print()
    else:
        print("✓✓✓ NO ISSUES FOUND - KETER IS PURE\n")

    if validation['recommendations']:
        print("Recommendations:")
        for i, rec in enumerate(validation['recommendations'], 1):
            print(f"{i}. {rec}")
        print()

    # Generate full report
    report_file = "KETER_PURITY_REPORT_venezuela.txt"
    report = generate_neutrality_report(VENEZUELA_CASE_NEUTRAL, report_file)
    print(f"✓ Full report saved: {report_file}\n")

    return 0 if validation['is_pure'] else 1

if __name__ == "__main__":
    exit(main())
