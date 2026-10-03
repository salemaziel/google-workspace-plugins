#!/usr/bin/env python3
"""
form_response_analyzer.py - Parse and summarize Google Forms responses JSON.

Usage:
  gws forms forms responses list --params '{"formId": "<formId>"}' | ./scripts/form_response_analyzer.py [--json]
"""

import sys
import json
import argparse
from collections import Counter, defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description="Analyze Google Forms responses JSON")
    parser.add_argument("--json", action="store_true", help="Output summary in JSON")
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            print("No JSON input provided on stdin.", file=sys.stderr)
            sys.exit(1)
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    responses = data if isinstance(data, list) else data.get("responses", [])
    total_responses = len(responses)

    if total_responses == 0:
        if args.json:
            print(json.dumps({"total_responses": 0, "questions": {}}))
        else:
            print("No responses received yet for this form.")
        return

    # Question ID -> list of answers
    q_answers = defaultdict(list)
    for r in responses:
        answers_dict = r.get("answers", {})
        for q_id, q_data in answers_dict.items():
            text_answers = q_data.get("textAnswers", {}).get("answers", [])
            for a in text_answers:
                val = a.get("value", "").strip()
                if val:
                    q_answers[q_id].append(val)

    analysis = {
        "total_responses": total_responses,
        "questions": {}
    }

    for q_id, ans_list in q_answers.items():
        counts = Counter(ans_list)
        analysis["questions"][q_id] = {
            "total_answers": len(ans_list),
            "distribution": dict(counts)
        }

    if args.json:
        print(json.dumps(analysis, indent=2))
    else:
        print(f"=== Form Response Analysis ({total_responses} Submissions) ===")
        for q_id, q_info in analysis["questions"].items():
            print(f"\nQuestion `{q_id}` ({q_info['total_answers']} replies):")
            for val, count in q_info["distribution"].items():
                pct = (count / total_responses) * 100
                print(f"  • {val:<35} : {count:>3} ({pct:>5.1f}%)")

if __name__ == "__main__":
    main()
