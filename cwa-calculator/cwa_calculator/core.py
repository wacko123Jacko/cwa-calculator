"""Core classes for computing a Cumulative Weighted Average (CWA)."""

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional


# Standard KNUST-style grade point scale.
DEFAULT_GRADE_SCALE: Dict[str, float] = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0,
}


@dataclass
class Course:
    """A single course result.

    Attributes:
        name: Course name or code (e.g. "ISD 378").
        credit_hours: Number of credit hours for the course.
        grade: Letter grade obtained (e.g. "A", "B+"), matched against
            the grade scale supplied to CWACalculator.
    """

    name: str
    credit_hours: float
    grade: str

    def __post_init__(self) -> None:
        if self.credit_hours <= 0:
            raise ValueError(
                f"credit_hours must be positive for course '{self.name}', "
                f"got {self.credit_hours}"
            )


class CWACalculator:
    """Computes Cumulative Weighted Average across one or more semesters."""

    def __init__(self, grade_scale: Optional[Dict[str, float]] = None):
        self.grade_scale = grade_scale or DEFAULT_GRADE_SCALE

    def _grade_point(self, grade: str) -> float:
        key = grade.strip().upper()
        if key not in self.grade_scale:
            valid = ", ".join(sorted(self.grade_scale))
            raise KeyError(f"Unknown grade '{grade}'. Valid grades: {valid}")
        return self.grade_scale[key]

    def compute(self, courses: Iterable[Course], round_to: int = 2) -> float:
        """Compute the CWA for a collection of courses.

        CWA = sum(credit_hours * grade_point) / sum(credit_hours)
        """
        courses = list(courses)
        if not courses:
            raise ValueError("At least one course is required to compute a CWA.")

        total_quality_points = 0.0
        total_credit_hours = 0.0

        for course in courses:
            gp = self._grade_point(course.grade)
            total_quality_points += gp * course.credit_hours
            total_credit_hours += course.credit_hours

        cwa = total_quality_points / total_credit_hours
        return round(cwa, round_to)

    def compute_by_semester(
        self, semesters: Dict[str, List[Course]], round_to: int = 2
    ) -> Dict[str, float]:
        """Compute a CWA for each semester, plus an overall 'Cumulative' entry."""
        results: Dict[str, float] = {}
        all_courses: List[Course] = []

        for label, courses in semesters.items():
            results[label] = self.compute(courses, round_to=round_to)
            all_courses.extend(courses)

        results["Cumulative"] = self.compute(all_courses, round_to=round_to)
        return results
