#!/usr/bin/env python3
from datetime import datetime

def get_next_month():
    now = datetime.now()
    month = (now.month % 12) + 1
    year = now.year + (1 if now.month == 12 else 0)
    month_name = datetime(year, month, 1).strftime('%B %Y')
    return month_name

if __name__ == '__main__':
    print(get_next_month())
