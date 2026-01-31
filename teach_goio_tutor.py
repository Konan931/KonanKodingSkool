#!/usr/bin/env python3
"""Interactive Tutor for teach_goio.py

Features:
- Static checks for teach_goio.py
- Interactive quiz with scoring
- Grading system that prints grades also in hex/octal/binary representations
- Optional colored output via 'rich' (falls installed)
- Side-story narration (Konan Koding Skool Berlin)
"""
import argparse
import importlib.util
import json
import re
from pathlib import Path
from datetime import datetime


SRC = Path(__file__).with_name('teach_goio.py')


try:
    from rich.console import Console
    from rich.markdown import Markdown
    console = Console()
    use_rich = True
except Exception:
    console = None
    use_rich = False


def read_src():
    return SRC.read_text(encoding='utf-8')


def find_issues(src: str):
    issues = []
    # stray token 'tz'
    if re.search(r'^\s*tz\s*$', src, flags=re.M):
        issues.append("Stray token 'tz' on its own line; remove it.")

    # bad except usage
    if re.search(r"except\s+Exception\s*:\s*\".*\"", src):
        issues.append("Invalid except usage: a string literal after except is wrong. Use a block with print().")

    # units attached to numbers
    if '6cm' in src or 'cm)' in src:
        issues.append("Found '6cm' or similar: units must not be appended to numeric literals in Python.")

    # mixed tabs
    if '\t' in src:
        issues.append("File contains tab characters; prefer 4 spaces for indentation.")

    return issues


def grade_to_representations(grade: float):
    # Represent grade as integer*10 and show hex/oct/bin
    g_int = int(round(grade * 10))
    return {'grade': grade, 'as_int': g_int, 'hex': hex(g_int), 'oct': oct(g_int), 'bin': bin(g_int)}


def explain_binary_basics():
    text = (
        "Binary is base 2. Each digit is a bit (0 or 1).\n"
        "Walkthrough: 10001001 (binary) = 1*2^7 + 0*2^6 + 0*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 137 (decimal).\n"
        "We use hex and octal to compactly represent numbers: hex(137) = 0x89, oct(137) = 0o211.\n"
    )
    return text


def run_quiz(interactive=True):
    questions = [
        {
            'q': 'Why is "6cm" in Python a syntax error?',
            'choices': ['Python knows "cm" as unit', 'You cannot append letters to numeric literals', 'It is valid'],
            'a': 2,
        },
        {
            'q': 'What indentation style should you use?',
            'choices': ['4 spaces', 'tabs', 'mix of both'],
            'a': 1,
        },
        {
            'q': 'How do you catch exceptions properly?',
            'choices': ["except Exception: 'msg'", 'except Exception:\n    print("msg")', 'except:'],
            'a': 2,
        },
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        if use_rich:
            console.print(f"Q{i}: {q['q']}")
            for idx, ch in enumerate(q['choices'], 1):
                console.print(f"  {idx}) {ch}")
            ans = console.input('Your answer (1/2/3): ')
        else:
            print(f"Q{i}: {q['q']}")
            for idx, ch in enumerate(q['choices'], 1):
                print(f"  {idx}) {ch}")
            ans = input('Your answer (1/2/3): ')
        try:
            if int(ans.strip()) == q['a']:
                score += 1
        except Exception:
            pass

    return score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--quiz', action='store_true', help='Run interactive quiz')
    parser.add_argument('--show-binary-basics', action='store_true', help='Show binary basics explanation')
    args = parser.parse_args()

    src = read_src()
    issues = find_issues(src)

    header = f"Konan Koding Skool Berlin — Tutor run at {datetime.utcnow().isoformat()}"
    if use_rich:
        console.rule(header)
    else:
        print(header)

    if issues:
        if use_rich:
            console.print('[bold red]Issues found in teach_goio.py:[/bold red]')
            for it in issues:
                console.print(f" - {it}")
        else:
            print('Issues found in teach_goio.py:')
            for it in issues:
                print(' -', it)
    else:
        if use_rich:
            console.print('[green]No obvious issues found.[/green]')
        else:
            print('No obvious issues found.')

    # show binary basics if requested
    if args.show_binary_basics:
        bb = explain_binary_basics()
        if use_rich:
            console.print(Markdown('''### Binary Basics\n'''))
            console.print(bb)
        else:
            print('\nBinary Basics:\n')
            print(bb)

    # short side story and rules
    story = (
        "Welcome to Konan Koding Skool Berlin. This is an elite and strict school,\n"
        "but it cares deeply about making you a master coder.\n"
        "Rule 1: Raise your hand when you want to speak.\n"
        "Rule 2: Stop whipping the chair — this is about your future, are you aware?\n"
    )
    if use_rich:
        console.print(story)
    else:
        print(story)

    if args.quiz:
        score = run_quiz()
        if use_rich:
            console.print(f"Quiz score: {score}/3")
        else:
            print(f"Quiz score: {score}/3")
        reps = grade_to_representations( (3-score) + 1 )
        # Map score to grade roughly
        grade = {3:1.0, 2:2.0, 1:3.0, 0:5.0}.get(score, 5.0)
        rep = grade_to_representations(grade)
        if use_rich:
            console.print(f"Grade: {rep['grade']} (int:{rep['as_int']}, hex:{rep['hex']}, oct:{rep['oct']}, bin:{rep['bin']})")
        else:
            print(f"Grade: {rep['grade']} (int:{rep['as_int']}, hex:{rep['hex']}, oct:{rep['oct']}, bin:{rep['bin']})")


if __name__ == '__main__':
    main()
    print('\nJetzt ein kurzes Quiz (3 Fragen). Antworte mit 1, 2 oder 3.')
    score = 0
    q1 = input('1) Warum ist "6cm" in Python ein Fehler?\n 1) Python kennt cm als Einheit\n 2) Zahlen dürfen keine Buchstaben direkt anhängen\ 3) Es ist gültig\> ')
    if q1.strip() == '2':
        score += 1
    q2 = input('2) Was soll man statt Tabs verwenden?\n 1) 4 Leerzeichen\ 2) 2 Tabs\ 3) Mix aus beidem\> ')
    if q2.strip() == '1':
        score += 1
    q3 = input('3) Wie fängt man ein except richtig an?\n 1) except Exception: "msg"\ 2) except Exception:\n    print("msg")\ 3) except:\n> ')
    if q3.strip() == '2':
        score += 1

    print(f'Your score: {score}/3')
    if score == 3:
        print('Ausgezeichnet. Note: 1')
    elif score == 2:
        print('Gute Arbeit. Note: 2')
    elif score == 1:
        print('Mehr üben. Note: 3')
    else:
        print('Nochmals üben. Note: 5')


if __name__ == '__main__':
    main()
