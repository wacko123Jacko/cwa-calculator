# cwa-calculator

A lightweight Python library for computing a student's **Cumulative Weighted
Average (CWA)** from course grades and credit hours, using the standard
KNUST-style grade-point scale (customizable).

## Install (local)

```bash
pip install -e .
```

## Usage

```python
from cwa_calculator import Course, CWACalculator

courses = [
    Course(name="ISD 378", credit_hours=3, grade="A"),
    Course(name="Company Law", credit_hours=3, grade="B+"),
    Course(name="Business Research Methods", credit_hours=2, grade="B"),
]

calc = CWACalculator()
print(calc.compute(courses))  # -> 3.32
```

### Per-semester breakdown

```python
semesters = {
    "Year 1 Sem 1": [Course("A", 3, "A"), Course("B", 3, "B")],
    "Year 1 Sem 2": [Course("C", 3, "B+")],
}
print(calc.compute_by_semester(semesters))
```

## Running tests

```bash
pip install pytest
pytest
```

## License

MIT
