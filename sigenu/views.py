from typing import Final

from django.db.models.functions import MD5
from django.db.models import CharField, Count, F, OuterRef, Value
from django.db.models.functions import Cast, Coalesce, Concat, Replace
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from sigenu import serializers
from sigenu.filterset import StudentFilterSet
from sigenu.models import Groups2Students, Student

ACTIVE_STATUS_VALUE: Final[str] = "02"


HASH_SUBQUERY: Final = MD5(
    Replace(
        Concat(
            Coalesce(F("name"), Value("None"), output_field=CharField()),
            Coalesce(F("middle_name"), Value("None"), output_field=CharField()),
            Coalesce(F("last_name"), Value("None"), output_field=CharField()),
            Coalesce(F("country__name"), Value("None"), output_field=CharField()),
            Coalesce(
                F("student_type__kind"),
                Value("None"),
                output_field=CharField(),
            ),
            Coalesce(
                F("career__national_career__name"),
                Value("None"),
                output_field=CharField(),
            ),
            Coalesce(F("faculty__name"), Value("None"), output_field=CharField()),
            Coalesce(
                F("course_type__name"),
                Value("None"),
                output_field=CharField(),
            ),
            Coalesce(
                F("scholastic_origin__name"),
                Value("None"),
                output_field=CharField(),
            ),
            Coalesce(
                F("town_university__town__name"),
                Value("None"),
                output_field=CharField(),
            ),
            Coalesce(
                Cast(
                    F("faculty__university__matriculation_end_date"),
                    output_field=CharField(),
                ),
                Value("None"),
                output_field=CharField(),
            ),
            Coalesce(
                Cast(
                    F("faculty__university__rematriculation_end_date"),
                    output_field=CharField(),
                ),
                Value("None"),
                output_field=CharField(),
            ),
        ),
        text=Value(" "),
        replacement=Value(""),
    )
)


class StudentViewSet(ListAPIView, GenericViewSet):
    """View to handle the student information"""

    queryset = (
        Student.objects.annotate(
            type_of_student=F("student_type__kind"),
            source_of_entry=F("entry_source__name"),
            type_of_course_name=F("course_type__name"),
            type_of_course_short_name=F("course_type__short_name"),
            scholastic_origin_name=F("scholastic_origin__name"),
            skin_color_name=F("skin_color__name"),
            country_name=F("country__name"),
            student_sex=F("sex__kind"),
            student_marital_status=F("marital_status__kind"),
            student_study_regimen=F("study_regimen__name"),
            student_politic_org=F("politic_org__name"),
            student_academic_situation=F("academic_situation__name"),
            student_orphan=F("orphan__kind"),
            year=Groups2Students.objects.filter(
                students_fk=OuterRef("pk"),
                groups_fk__career_fk=OuterRef("career"),
                groups_fk__course_fk=OuterRef("career__faculty__university__course"),
                consecutive="0",
            )
            .annotate(year=F("groups_fk__year"))
            .values("year"),
            hash=HASH_SUBQUERY,
        )
        .select_related(
            "career",
            "career__national_career",
            "career__national_career__scienc_especialty",
            "faculty",
        )
        .order_by("-fixed_register_date", "identification")
        .only(
            "identification",
            "name",
            "middle_name",
            "last_name",
            "native_of",
            "birth_date",
            "address",
            "phone",
            "email",
            "register_date",
            # ForeignKeys
            "career__national_career__name",
            "career__national_career__code",
            "career__national_career__diploma",
            "career__national_career__scienc_especialty__name",
            "faculty__id_faculty",
            "faculty__name",
            "faculty__address",
            "faculty__phone_number",
        )
    )
    serializer_class = serializers.StudentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = StudentFilterSet
    ordering_fields = (
        "identification",
        "name",
        "middle_name",
        "last_name",
        "birth_date",
        "register_date",
    )

    @action(
        detail=True,
    )
    def search_by_dni(self, *args, **kwargs):
        return Response(
            data=self.serializer_class(
                instance=get_object_or_404(
                    self.get_queryset(), **{"identification": kwargs[self.lookup_field]}
                )
            ).data
        )

    @action(
        detail=False,
    )
    def counts(self, *args, **kwargs) -> JsonResponse:
        students = Student.objects.filter(student_status=ACTIVE_STATUS_VALUE)
        return Response(
            {
                "by_faculty": list(
                    students.values("faculty")
                    .annotate(count=Count("pk"), faculty_name=F("faculty__name"))
                    .order_by("-count")
                ),
                "by_career": list(
                    students.values("career")
                    .annotate(
                        count=Count("pk"),
                        career_name=F("career__national_career__name"),
                    )
                    .order_by("-count")
                ),
                "by_course_type": list(
                    students.values("course_type")
                    .annotate(
                        count=Count("pk"), course_type_name=F("course_type__name")
                    )
                    .order_by("-count")
                ),
                "by_year": list(
                    students.annotate(
                        year=Groups2Students.objects.filter(
                            students_fk=OuterRef("pk"),
                            groups_fk__career_fk=OuterRef("career"),
                            groups_fk__course_fk=OuterRef(
                                "career__faculty__university__course"
                            ),
                            consecutive="0",
                        )
                        .annotate(year=F("groups_fk__year"))
                        .values("year"),
                    )
                    .values("year")
                    .annotate(count=Count("pk"))
                    .order_by("-count")
                ),
            }
        )
