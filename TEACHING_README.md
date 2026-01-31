Teaching materials for CoderClass

This folder contains:
- `teach_goio.py` — example script (areas, datetime examples)
- `teach_goio_tutor.py` — interactive tutor that inspects `teach_goio.py`, gives corrections and a short quiz

How to use:
1. Run the tutor interactively:

```bash
cd .vscode/Sololearn/CoderClass
python3 teach_goio_tutor.py
```

2. Run the example script to see the grading/story output:

```bash
python3 teach_goio.py
```

Objectives:
- Find and fix syntax issues (e.g. invalid numeric literals like `6cm`)
- Avoid mixing tabs and spaces
- Understand proper `except` syntax and error handling
- Practice small quizzes and learn from the teacher's feedback

Grading rubric (simple):
- 0 issues -> Note 1.0 (Sehr gut)
- 1 issue  -> Note 2.0 (Gut)
- 2 issues -> Note 3.0 (Befriedigend)
- 3 issues -> Note 4.0 (Ausreichend)
- >=4 issues -> Note 5.0 (Nicht bestanden)

Conversion utilities:
- `teach_goio.py` demonstrates parsing a class tag like `#h/10001001` and prints decimal/hex/octal/binary representations.

Story:
- The tutor presents a short, strict story to set classroom tone; use it as a narrative device to explain discipline in coding.
