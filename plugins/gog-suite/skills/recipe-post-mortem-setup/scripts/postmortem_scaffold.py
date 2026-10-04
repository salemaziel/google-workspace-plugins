#!/usr/bin/env python3
import sys

def template(incident):
    return f"""# Incident Post-Mortem: {incident}

## Executive Summary
Brief non-technical overview of the outage and impact.

## Timeline (UTC)
- HH:MM: Issue detected
- HH:MM: Mitigation deployed
- HH:MM: Full recovery

## Root Cause Analysis
5 Whys breakdown of architectural contributing factors.

## Action Items
- [ ] Action item 1 (Owner: Eng)
"""

if __name__ == '__main__':
    inc = sys.argv[1] if len(sys.argv) > 1 else 'INC-2026-01'
    print(template(inc))
