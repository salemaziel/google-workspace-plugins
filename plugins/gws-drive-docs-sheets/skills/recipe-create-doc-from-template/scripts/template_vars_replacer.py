#!/usr/bin/env python3
import sys

def fill_template(raw, project, author):
    return raw.replace('{{PROJECT}}', project).replace('{{AUTHOR}}', author)

if __name__ == '__main__':
    print("Template substitution utility ready.")
