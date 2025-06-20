from rest_framework import serializers

from sigenu.models import Career, Faculty, Student


class FacultySerializer(serializers.ModelSerializer):
    id_faculty = serializers.CharField()
    name = serializers.CharField()
    address = serializers.CharField()
    phone_number = serializers.CharField()

    class Meta:
        model = Faculty
        fields = ("id_faculty", "name", "address", "phone_number")


class StudentCareerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="national_career.name")
    code = serializers.CharField(source="national_career.code")
    specialty = serializers.CharField(source="national_career.scienc_especialty.name")
    diploma = serializers.CharField(source="national_career.diploma")

    class Meta:
        model = Career
        fields = (
            "name",
            "code",
            "specialty",
            "diploma",
        )


class StudentSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(source="fixed_birth_date")
    register_date = serializers.DateTimeField(source="fixed_register_date")
    student_type = serializers.CharField(source="type_of_student")
    entry_source = serializers.CharField(source="source_of_entry")
    course_type_name = serializers.CharField(source="type_of_course_name")
    course_type_short_name = serializers.CharField(source="type_of_course_short_name")
    scholastic_origin = serializers.CharField(source="scholastic_origin_name")
    skin_color = serializers.CharField(source="skin_color_name")
    country = serializers.CharField(source="country_name")
    sex = serializers.CharField(source="student_sex")
    marital_status = serializers.CharField(source="student_marital_status")
    study_regimen = serializers.CharField(source="student_study_regimen")
    politic_org = serializers.CharField(source="student_politic_org")
    academic_situation = serializers.CharField(source="student_academic_situation")
    orphan = serializers.CharField(source="student_orphan")
    hash = serializers.CharField()
    year = serializers.CharField()
    career = StudentCareerSerializer()
    faculty = FacultySerializer()

    class Meta:
        model = Student
        fields = (
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
            "hash",
            # Related Models
            "student_type",
            "entry_source",
            "course_type_name",
            "course_type_short_name",
            "scholastic_origin",
            "skin_color",
            "country",
            "sex",
            "marital_status",
            "study_regimen",
            "politic_org",
            "academic_situation",
            "orphan",
            "year",
            # ForeignKeys
            "career",
            "faculty",
        )
