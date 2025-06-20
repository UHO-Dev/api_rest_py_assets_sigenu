from django_filters.rest_framework.filters import ChoiceFilter, ModelChoiceFilter
from django_filters.rest_framework.filterset import FilterSet

from sigenu.models import (
    Career,
    CourseType,
    Faculty,
    Student,
    StudentStatus,
    StudentType,
)


class StudentFilterSet(FilterSet):
    student_type = ModelChoiceFilter(queryset=StudentType.objects.all())
    student_status = ModelChoiceFilter(queryset=StudentStatus.objects.all())
    faculty = ModelChoiceFilter(queryset=Faculty.objects.all())
    career = ModelChoiceFilter(queryset=Career.objects.all())
    year = ChoiceFilter(
        choices=[
            (None, "None"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
        ],
        label="Year",
    )
    course_type = ModelChoiceFilter(queryset=CourseType.objects.all())

    class Meta:
        model = Student
        fields = (
            "identification",
            "name",
            "middle_name",
            "last_name",
            "birth_date",
            "register_date",
        )
