# Calculating areas - the basics
# Class h/10001001a

import os
import sys
from datetime import datetime, timezone, timedelta
import math
import time as _time

# Robust timezone setup: prefer tzset on POSIX, otherwise rely on zoneinfo-aware datetimes
os.environ['TZ'] = 'UTC'
if hasattr(_time, 'tzset'):
	for tz_choice in ('UTC', 'Etc/UTC', 'GMT'):
		os.environ['TZ'] = tz_choice
		try:
			_time.tzset()
			break
		except Exception:
			# continue silently if tzset fails for this value
			continue
else:
	# tzset not available; zoneinfo will be used for aware datetimes
	pass

# Print some environment info for debugging purposes and teaching
# get current year in UTC for demonstration and logging as well as intercontinental classroom consistency
year = datetime.now(timezone.utc).year
year_of_code = 2024
# Compute pupil's learning year/age relative to reference
# Reference pupil age in 2024 is 13 years
reference_pupil_age = 13
pupil_age = reference_pupil_age + (year - year_of_code)
year_of_learning = year_of_code
print(f"Pupil is learning in the year: {year_of_learning}, Age: {pupil_age} years")

from zoneinfo import ZoneInfo  # Python >=3.9

# Class demonstration of datetime features

# Lecture 1: datetime basics

# naive current local time
now_local = datetime.now()

# aware current UTC
now_utc = datetime.now(timezone.utc)

# aware with zoneinfo
berlin = datetime.now(ZoneInfo("Europe/Berlin"))

# get pupils timezone
pupil_tz = ZoneInfo("UTC")  # default to UTC for demo; replace with real tz when known
pupil_time = datetime.now(pupil_tz)
print("Pupil's local time sample:", pupil_time)

# create specific datetime
d = datetime(2024, 1, 31, 15, 30, 0)

# parsing/format
s = d.isoformat()            # '2024-01-31T15:30:00'
d2 = datetime.fromisoformat(s)
fmt = d.strftime("%Y-%m-%d %H:%M:%S")

# utc offset zone
tz_plus = timezone(timedelta(hours=2))
d3 = datetime(2024, 1, 31, 12, 0, tzinfo=tz_plus)

# arithmetic
d4 = d + timedelta(days=7)
print("Pupil is learning in the current year:", year)

# print environment info
print("Current UTC year:", year)
print("Python version:", sys.version)
print("Platform:", sys.platform)
print("OS name:", os.name)
print("Current working directory:", os.getcwd())
print("Environment TZ:", os.environ.get('TZ', 'not set'))





# Basic class definition

class MisterKonan:
	"""A strict instructor. Tough but fair.

	MisterKonan scolds the pupil, grades results and can explain mistakes.
	He also stores a 'binary_name' tag used in the side story.
	"""
	def __init__(self, coder, binary_name='10001001'):
		self.coder = coder
		# binary_name is stored as a string containing 0/1 sequence
		self.binary_name = binary_name

	def informatics_test(self, shape, calculate='area', **kwargs):
		if calculate != 'area':
			raise ValueError("Only 'area' calculation is supported")
		# Dispatch to helper functions
		if shape == 'rectangle':
			width = kwargs.get('width', 0)
			height = kwargs.get('height', 0)
			return area_rectangle(width, height)
		elif shape == 'circle':
			radius = kwargs.get('radius', 0)
			return area_circle(radius)
		elif shape == 'triangle':
			base = kwargs.get('base', 0)
			height = kwargs.get('height', 0)
			return area_triangle(base, height)
		elif shape == 'square':
			side = kwargs.get('side', 0)
			return area_square(side)
		elif shape == 'ellipse':
			a = kwargs.get('a', 0)
			b = kwargs.get('b', 0)
			return area_ellipse(a, b)
		else:
			raise ValueError(f"Unknown shape type: {shape}")

	def scold(self, message: str):
		print(f"MisterKonan (stern): {message}")

	def grade(self, issues: int):
		# strict grading: fewer issues => better grade
		if issues == 0:
			return 1.0
		if issues == 1:
			return 2.0
		if issues == 2:
			return 3.0
		if issues == 3:
			return 4.0
		return 5.0

	def binary_name_info(self):
		# interpret binary_name
		try:
			n = int(self.binary_name, 2)
		except Exception:
			n = 0
		return {'bin': self.binary_name, 'dec': n, 'hex': hex(n), 'oct': oct(n)}

fail_log = """
 File "./Playground/file0.py", line 25
	base=(6cm)
		  ^
SyntaxError: invalid decimal literal
"""


def parse_and_convert_classname(tag: str):
	"""Parse a class tag like '#h/10001001' and print conversions.

	The function tries to interpret the part after '/' as binary if it contains only 0/1,
	otherwise as decimal. Returns a dict with multiple representations.
	"""
	out = {}
	out['tag'] = tag
	if '/' in tag:
		_, val = tag.split('/', 1)
	else:
		val = tag

	# strip non-alphanum
	import re as _re
	v = _re.sub(r'[^0-9A-Fa-f]', '', val)

	# If original contains only 0/1 characters, treat as binary
	raw = val
	if all(ch in '01' for ch in raw):
		n = int(raw, 2)
	else:
		# try decimal first, then hex
		try:
			n = int(raw, 10)
		except Exception:
			try:
				n = int(raw, 16)
			except Exception:
				n = 0

	out['dec'] = n
	out['hex'] = hex(n)
	out['oct'] = oct(n)
	out['bin'] = bin(n)
	# as bytes (big endian for common display)
	try:
		b = n.to_bytes((n.bit_length() + 7) // 8 or 1, 'big')
		out['bytes_hex'] = b.hex()
		try:
			out['as_ascii'] = b.decode('ascii')
		except Exception:
			out['as_ascii'] = None
	except Exception:
		out['bytes_hex'] = None
		out['as_ascii'] = None

	return out


def strict_grade(issues_count: int, pupil_age: int):
	"""Return a grade and stern message depending on issues_count."""
	# simple grading scale: 0 issues -> 1.0, 1->2.0, 2->3.0, >=4 -> 5.0
	if issues_count == 0:
		grade = 1.0
	elif issues_count == 1:
		grade = 2.0
	elif issues_count == 2:
		grade = 3.0
	elif issues_count == 3:
		grade = 4.0
	else:
		grade = 5.0

	# stern message (English)
	if grade <= 2.0:
		msg = "Well done, but pay more attention to details!"
	else:
		msg = "Very strict: You must check your inputs and comment clearly."

	# theatrical story element (English)
	story = (
		"The teacher slams his bag down on the chair and looks over the rim.",
		" 'What a mess!', he says. 'Next time I expect clean code.'"
	)

	return {'grade': grade, 'message': msg, 'story': ' '.join(story), 'pupil_age': pupil_age}


# --- Area helper functions ---
def area_rectangle(width: float, height: float) -> float:
	return float(width) * float(height)


def area_circle(radius: float) -> float:
	return math.pi * float(radius) ** 2


def area_triangle(base: float, height: float) -> float:
	return 0.5 * float(base) * float(height)


def area_square(side: float) -> float:
	return float(side) ** 2


def area_ellipse(a: float, b: float) -> float:
	# ellipse area = pi * a * b (a and b are semi-axes)
	return math.pi * float(a) * float(b)


class Pupil:
	"""Simple pupil model for the teaching demo."""
	def __init__(self, name: str, age: int):
		self.name = name
		self.age = age
		self.mistakes = 0
		self.attempts = 0

	def attempt(self, func, *args, **kwargs):
		self.attempts += 1
		try:
			result = func(*args, **kwargs)
			return result
		except Exception as e:
			self.mistakes += 1
			return f"Error: {e}"

if __name__ == '__main__':
	# Setup teacher and pupil
	mk = MisterKonan('Prof. Dr. Konan Sternbernt', binary_name='10001001')
	pupil = Pupil('Young Coder', pupil_age)

	print("Teacher:", mk.coder)
	print("Pupil:", pupil.name, "Age:", pupil.age)

	# Lesson 1: basics. Start slow and explain each shape.
	print('\nLesson 1: Basic areas (step-by-step)')
	print(' - Rectangle 3x4: expected 12')
	res = pupil.attempt(mk.informatics_test, 'rectangle', width=3, height=4)
	print('   Result:', res)

	print(' - Circle r=2: expected approx 12.566')
	res = pupil.attempt(mk.informatics_test, 'circle', radius=2)
	print('   Result:', res)

	print(' - Triangle base=6 height=4: expected 12')
	res = pupil.attempt(mk.informatics_test, 'triangle', base=6, height=4)
	print('   Result:', res)

	# Lesson 2: extended shapes
	print('\nLesson 2: Extended shapes')
	print(' - Square side=5: expected 25')
	print('   Result:', pupil.attempt(mk.informatics_test, 'square', side=5))
	print(' - Ellipse a=3 b=2: expected approx', math.pi * 3 * 2)
	print('   Result:', pupil.attempt(mk.informatics_test, 'ellipse', a=3, b=2))

	# Show class tag conversions with explanation
	print('\nClass tag conversion and story:')
	tag = '#h/10001001'
	conv = parse_and_convert_classname(tag)
	print(f" The tag {conv['tag']} is interpreted as decimal {conv['dec']}, hex {conv['hex']}, octal {conv['oct']}, binary {conv['bin']}")
	if conv.get('as_ascii'):
		print(' ASCII view:', conv['as_ascii'])
	else:
		print(' ASCII view: (non-printable)')

	# Teacher binary name side story
	print('\nTeacher binary-name info:')
	print(mk.binary_name_info())
	print('\nSide story:')
	print(' MisterKonan has a binary name. He explains the code by converting that name to numbers and asking the pupil to trace bits.')

	# Evaluate pupil and grade
	issues = pupil.mistakes
	print(f"\nPupil attempts: {pupil.attempts}, mistakes recorded: {pupil.mistakes}")
	grade = mk.grade(issues)
	report = strict_grade(issues, pupil.age)
	print('\n--- Evaluation ---')
	print('Pupil age (calculated):', report['pupil_age'])
	print('Numeric grade:', report['grade'])
	print('Teacher message:', report['message'])
	print('\nStory:')
	print(report['story'])
