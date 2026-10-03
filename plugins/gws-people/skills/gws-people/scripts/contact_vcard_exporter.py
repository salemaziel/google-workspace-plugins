#!/usr/bin/env python3
"""
contact_vcard_exporter.py - Convert Google People connections JSON into standard CSV or vCard (.vcf).

Usage:
  gws people people connections list --params '{"resourceName": "people/me", "personFields": "names,emailAddresses,phoneNumbers,organizations"}' | ./scripts/contact_vcard_exporter.py [--format csv|vcf]
"""

import sys
import json
import csv
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Export Google Contacts JSON to CSV or vCard")
    parser.add_argument("--format", choices=["csv", "vcf", "table"], default="table", help="Output format")
    return parser.parse_args()

def extract_contact(p):
    names = p.get("names", [])
    display_name = names[0].get("displayName", "Unnamed") if names else "Unnamed"
    given_name = names[0].get("givenName", "") if names else ""
    family_name = names[0].get("familyName", "") if names else ""

    emails = [e.get("value", "") for e in p.get("emailAddresses", [])]
    primary_email = emails[0] if emails else ""

    phones = [ph.get("value", "") for ph in p.get("phoneNumbers", [])]
    primary_phone = phones[0] if phones else ""

    orgs = p.get("organizations", [])
    title = orgs[0].get("title", "") if orgs else ""
    company = orgs[0].get("name", "") if orgs else ""

    return {
        "resourceName": p.get("resourceName", ""),
        "name": display_name,
        "givenName": given_name,
        "familyName": family_name,
        "email": primary_email,
        "phone": primary_phone,
        "title": title,
        "company": company
    }

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

    connections = data if isinstance(data, list) else data.get("connections", [])
    contacts = [extract_contact(c) for c in connections]

    if args.format == "csv":
        writer = csv.DictWriter(sys.stdout, fieldnames=["name", "email", "phone", "title", "company", "resourceName"])
        writer.writeheader()
        for c in contacts:
            writer.writerow({
                "name": c["name"],
                "email": c["email"],
                "phone": c["phone"],
                "title": c["title"],
                "company": c["company"],
                "resourceName": c["resourceName"]
            })
    elif args.format == "vcf":
        for c in contacts:
            print("BEGIN:VCARD")
            print("VERSION:3.0")
            print(f"FN:{c['name']}")
            print(f"N:{c['familyName']};{c['givenName']};;;")
            if c["email"]:
                print(f"EMAIL;TYPE=INTERNET:{c['email']}")
            if c["phone"]:
                print(f"TEL;TYPE=CELL:{c['phone']}")
            if c["company"] or c["title"]:
                print(f"ORG:{c['company']}")
                print(f"TITLE:{c['title']}")
            print("END:VCARD\n")
    else:
        # Table
        if not contacts:
            print("No contacts found.")
            return
        print(f"{'Name':<25} | {'Email':<30} | {'Company / Title'}")
        print("-" * 75)
        for c in contacts:
            role = f"{c['title']} @ {c['company']}".strip(" @")
            print(f"{c['name']:<25} | {c['email']:<30} | {role}")

if __name__ == "__main__":
    main()
