#!/usr/bin/env python3
import sys, json

def scaffold_question(title):
    return {
        'title': title,
        'questionItem': {
            'question': {
                'required': True,
                'textQuestion': {'paragraph': True}
            }
        }
    }

if __name__ == '__main__':
    t = sys.argv[1] if len(sys.argv) > 1 else 'Any additional comments?'
    print(json.dumps(scaffold_question(t), indent=2))
