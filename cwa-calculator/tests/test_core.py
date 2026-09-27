import pytest

from cwa_calculator import Course, CWACalculator


def test_single_course_cwa_equals_its_grade_point():
    calc = CWACalculator()
    result = calc.compute([Course("ISD 378", 3, "A")])
    assert result == 4.0


def test_weighted_average_across_courses():
    calc = CWACalculator()
    courses = [
        Course("Company Law", 3, "B+"),   # 3 * 3.5 = 10.5
        Course("ISD 378", 3, "A"),        # 3 * 4.0 = 12.0
        Course("DBMS", 2, "B"),           # 2 * 3.0 = 6.0
    ]
    # total quality points = 28.5, total credits = 8 -> 3.5625 -> 3.56
    assert calc.compute(courses) == 3.56


def test_unknown_grade_raises():
    calc = CWACalculator()
    with pytest.raises(KeyError):
        calc.compute([Course("X", 3, "Z")])


def test_zero_credit_hours_raises():
    with pytest.raises(ValueError):
        Course("X", 0, "A")


def test_empty_course_list_raises():
    calc = CWACalculator()
    with pytest.raises(ValueError):
        calc.compute([])


def test_compute_by_semester():
    calc = CWACalculator()
    semesters = {
        "Year 1 Sem 1": [Course("A", 3, "A"), Course("B", 3, "B")],
        "Year 1 Sem 2": [Course("C", 3, "B+")],
    }
    results = calc.compute_by_semester(semesters)
    assert "Cumulative" in results
    assert results["Year 1 Sem 1"] == 3.5
