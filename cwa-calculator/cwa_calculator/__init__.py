"""
cwa_calculator
==============

A lightweight Python library for computing a student's Cumulative
Weighted Average (CWA) from course grades and credit hours.

Typical KNUST-style grading is supported out of the box (A=4.0, B+=3.5,
B=3.0, C+=2.5, C=2.0, D+=1.5, D=1.0, F=0.0), but a custom grade-point
scale can be supplied.

Example
-------
>>> from cwa_calculator import Course, CWACalculator
>>> courses = [
...     Course(name="ISD 378", credit_hours=3, grade="A"),
...     Course(name="Company Law", credit_hours=3, grade="B+"),
...     Course(name="Business Research Methods", credit_hours=2, grade="B"),
... ]
>>> calc = CWACalculator()
>>> calc.compute(courses)
3.32
"""

from .core import Course, CWACalculator, DEFAULT_GRADE_SCALE

__all__ = ["Course", "CWACalculator", "DEFAULT_GRADE_SCALE"]
__version__ = "1.0.0"
