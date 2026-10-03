#!/usr/bin/env python3
"""
chat_card_builder.py - Generate Google Chat Cards v2 JSON payloads for `gws chat spaces messages create`.

Usage:
  ./scripts/chat_card_builder.py --title "Deployment Complete" --subtitle "Production v2.4.0" --kv "Author=salemaziel" --kv "Status=Success" --button "Logs=https://ci.example.com"
"""

import sys
import json
import argparse
import uuid

def parse_args():
    parser = argparse.ArgumentParser(description="Build Google Chat Cards v2 JSON")
    parser.add_argument("--title", required=True, help="Card header title")
    parser.add_argument("--subtitle", help="Card header subtitle")
    parser.add_argument("--kv", action="append", default=[], help="Key=Value attribute lines")
    parser.add_argument("--button", action="append", default=[], help="Label=URL button links")
    return parser.parse_args()

def main():
    args = parse_args()
    
    widgets = []
    for item in args.kv:
        if "=" in item:
            k, v = item.split("=", 1)
            widgets.append({
                "decoratedText": {
                    "topLabel": k.strip(),
                    "text": v.strip()
                }
            })
        else:
            widgets.append({
                "textParagraph": {
                    "text": item.strip()
                }
            })

    if args.button:
        button_items = []
        for btn in args.button:
            if "=" in btn:
                lbl, url = btn.split("=", 1)
                button_items.append({
                    "text": lbl.strip(),
                    "onClick": {
                        "openLink": {"url": url.strip()}
                    }
                })
        if button_items:
            widgets.append({"buttonList": {"buttons": button_items}})

    card_payload = {
        "cardsV2": [
            {
                "cardId": f"card-{uuid.uuid4().hex[:8]}",
                "card": {
                    "header": {
                        "title": args.title,
                        "subtitle": args.subtitle or ""
                    },
                    "sections": [
                        {
                            "widgets": widgets
                        }
                    ]
                }
            }
        ]
    }

    print(json.dumps(card_payload, indent=2))

if __name__ == "__main__":
    main()
