from rest_framework import serializers

from sigenu.models import (
    AcademicSituation,
    Career,
    Country,
    Course,
    CourseType,
    EntrySource,
    Faculty,
    Groups2Students,
    Groups2StudentsHash,
    MaritalStatus,
    NationalCareer,
    Orphan,
    PoliticOrg,
    Province,
    ScholasticOrigin,
    SciencEspecialty,
    Sex,
    SkinColor,
    Student,
    StudentHash,
    StudentStatus,
    StudentType,
    StudyProgram,
    StudyRegimen,
    Town,
    TownUniversity,
    University,
    Xgroup,
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StudentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentType
        fields = "__all__"


class SciencEspecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = SciencEspecialty
        fields = "__all__"


class NationalCareerSerializer(serializers.ModelSerializer):
    scienc_especialty = SciencEspecialtySerializer()

    class Meta:
        model = NationalCareer
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class TownSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()

    class Meta:
        model = Town
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):
    town = TownSerializer()
    course = CourseSerializer()

    class Meta:
        model = University
        fields = "__all__"


class TownUniversitySerializer(serializers.ModelSerializer):
    town = TownSerializer()
    university = UniversitySerializer()

    class Meta:
        model = TownUniversity
        fields = "__all__"


class FacultySerializer(serializers.ModelSerializer):
    town = TownSerializer()
    university = UniversitySerializer()

    class Meta:
        model = Faculty
        fields = "__all__"


#######################################################################


class FacultyCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        # fields = "__all__"
        fields = ["id_faculty", "name", "career_faculty"]
        depth = 2


########################################################################


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = "__all__"


class CareerSerializer(serializers.ModelSerializer):
    national_career = NationalCareerSerializer()
    town_university = TownUniversitySerializer()
    faculty = FacultySerializer()
    course_type = CourseTypeSerializer()

    class Meta:
        model = Career
        fields = "__all__"


class EntrySourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrySource
        fields = "__all__"


class ScholasticOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholasticOrigin
        fields = "__all__"


class PoliticOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticOrg
        fields = "__all__"


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = "__all__"


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = "__all__"


class StudyRegimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyRegimen
        fields = "__all__"


class StudentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentStatus
        fields = "__all__"


class AcademicSituationSerializer(serializers.ModelSerializer):
    student_status = StudentStatusSerializer()

    class Meta:
        model = AcademicSituation
        fields = "__all__"


class SkinColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinColor
        fields = "__all__"


class OrphanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orphan
        fields = "__all__"


class XgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xgroup
        # fields = ['group_fk', 'year', 'id_group']
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    student_type = StudentTypeSerializer()
    career = CareerSerializer()
    entry_source = EntrySourceSerializer()
    course_type = CourseTypeSerializer()
    scholastic_origin = ScholasticOriginSerializer()
    politic_org = PoliticOrgSerializer()
    sex = SexSerializer()
    town_university = TownUniversitySerializer()
    marital_status = MaritalStatusSerializer()
    study_regimen = StudyRegimenSerializer()
    academic_situation = AcademicSituationSerializer()
    town = TownSerializer()
    skin_color = SkinColorSerializer()
    student_status = StudentStatusSerializer()
    faculty = FacultySerializer()
    orphan = OrphanSerializer()

    class Meta:
        model = Student
        fields = "__all__"


class StudentSerializerLinked(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id_student", "identification", "name", "last_name", "middle_name"]


class StudyProgramSerializer(serializers.ModelSerializer):
    career = CareerSerializer()
    course = CourseSerializer()

    class Meta:
        model = StudyProgram
        fields = "__all__"


class Groups2StudentsSerializer(serializers.ModelSerializer):
    groups_fk = XgroupSerializer()
    students_fk = StudentSerializer()

    class Meta:
        model = Groups2Students
        fields = "__all__"
        # fields = ['students_fk', 'groups_fk', 'id', 'consecutive']


class Groups2StudentsHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups2StudentsHash
        fields = ["groups_fk", "id", "consecutive"]
        # fields = "__all__"


class StudentHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHash
        fields = ["identification", "name", "group_student"]
        depth = 2
