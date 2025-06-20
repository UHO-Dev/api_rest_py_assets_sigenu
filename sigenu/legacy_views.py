# import passlib.hash
import hashlib

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters, generics, viewsets

from sigenu import legacy_serializers
from sigenu.models import (
    AcademicSituation,
    Career,
    Country,
    CourseType,
    EntrySource,
    Faculty,
    Groups2Students,
    MaritalStatus,
    Orphan,
    PoliticOrg,
    ScholasticOrigin,
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
    Xgroup,
)


class StudentAllViewSet(viewsets.ModelViewSet):
    """Return all student, inactive and inactive"""

    queryset = Student.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.StudentSerializer


class StudentAllActiveViewSet(viewsets.ModelViewSet):
    """Return all student active"""

    queryset = Student.objects.using("sigenu_student").filter(student_status="02")
    serializer_class = legacy_serializers.StudentSerializer


class CountryViewSet(viewsets.ModelViewSet):
    """Return all Country"""

    queryset = Country.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.CountrySerializer


class StudentTypeViewSet(viewsets.ModelViewSet):
    """Return all StudentType"""

    queryset = StudentType.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.StudentTypeSerializer


class CareerViewSet(viewsets.ModelViewSet):
    """Return all Career"""

    queryset = Career.objects.using("sigenu_student").filter(cancelled="False")
    serializer_class = legacy_serializers.CareerSerializer


class EntrySourceViewSet(viewsets.ModelViewSet):
    """Return all EntrySource"""

    queryset = EntrySource.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.EntrySourceSerializer


class CourseTypeViewSet(viewsets.ModelViewSet):
    """Return all CourseType"""

    queryset = CourseType.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.CourseTypeSerializer


class ScholasticOriginViewSet(viewsets.ModelViewSet):
    """Return all ScholasticOrigin"""

    queryset = ScholasticOrigin.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.ScholasticOriginSerializer


class PoliticOrgViewSet(viewsets.ModelViewSet):
    """Return all PoliticOrg"""

    queryset = PoliticOrg.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.PoliticOrgSerializer


class SexViewSet(viewsets.ModelViewSet):
    """Return all Sex"""

    queryset = Sex.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.SexSerializer


class TownUniversityViewSet(viewsets.ModelViewSet):
    """Return all TownUniversity"""

    queryset = TownUniversity.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.TownUniversitySerializer


class MaritalStatusViewSet(viewsets.ModelViewSet):
    """Return all MaritalStatus"""

    queryset = MaritalStatus.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.MaritalStatusSerializer


class StudyRegimenViewSet(viewsets.ModelViewSet):
    """Return all StudyRegimen"""

    queryset = StudyRegimen.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.StudyRegimenSerializer


class AcademicSituationViewSet(viewsets.ModelViewSet):
    """Return all AcademicSituation"""

    queryset = AcademicSituation.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.AcademicSituationSerializer


class TownSituationViewSet(viewsets.ModelViewSet):
    """Return all Town"""

    queryset = Town.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.TownSerializer


class SkinColorViewSet(viewsets.ModelViewSet):
    """Return all SkinColor"""

    queryset = SkinColor.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.SkinColorSerializer


class StudentStatusViewSet(viewsets.ModelViewSet):
    """Return all StudentStatus"""

    queryset = StudentStatus.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.StudentStatusSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    """Return all Faculty active"""

    queryset = Faculty.objects.using("sigenu_student").filter(cancelled="False")
    serializer_class = legacy_serializers.FacultySerializer


class FacultyCareerViewSet(viewsets.ModelViewSet):
    """Return all Faculty active"""

    queryset = Faculty.objects.using("sigenu_student").filter(cancelled="False")
    serializer_class = legacy_serializers.FacultyCareerSerializer


class OrphanViewSet(viewsets.ModelViewSet):
    """Return all Orphan"""

    queryset = Orphan.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.OrphanSerializer


class StudyProgramViewSet(viewsets.ModelViewSet):
    """Return all StudyProgram"""

    queryset = StudyProgram.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.StudyProgramSerializer


class XgroupViewSet(viewsets.ModelViewSet):
    """Return all Xgroup"""

    queryset = Xgroup.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.XgroupSerializer


class Group2StudentViewSet(viewsets.ModelViewSet):
    """Return all Xgroup"""

    queryset = Groups2Students.objects.using("sigenu_student").all()
    serializer_class = legacy_serializers.Groups2StudentsSerializer


# class Groups2StudentsOneViewSet(viewsets.ModelViewSet):
#     """Return all Groups2Students"""
#
#     queryset = Groups2Students.objects.using("sigenu_student").all()
#     serializer_class = serializers.Groups2StudentsSerializer
#     lookup_field = 'pk'
#     # queryset = Groups2Students.objects.using("sigenu_student").
# filter(consecutive="0", students_fk__student_status="02", groups_fk__year= "2")
#
#     @action(detail=True)
#     def get_year(self, request, pk=None):
#         """
#         Returns a list of all the employees that have an identity card.
#         """
#         # user = self.get_object()
#         # groups = user.groups.all()
#         students = Groups2Students.objects.using("sigenu_student").
# filter(consecutive="0", students_fk__student_status="02", groups_fk__year = str(pk))
#         serializer = serializers.Groups2StudentsSerializer(students, many=True)
#
#         #return Response([group.name for group in groups])
#         return Response(serializer.data)

#####################################################################################################


# class TestViewSet(generics.ListAPIView):
#     """Return all Groups2Students 1"""
#
#     serializer_class = serializers.Groups2StudentsTestSerializer
#
#     def get_queryset(self):
#         """
#         Optionally restricts the returned faculty to a career,
#         by filtering against a `years` query parameter in the URL.
#         """
#
#         queryset = Groups2StudentsTest.objects.using("sigenu_student").
# filter(consecutive="0")
#
#         identification = self.request.query_params.get('identification')
#         student_status = self.request.query_params.get('student_status')
#         year = self.request.query_params.get('year')# group__year= "1"
#
#
#         if identification is not None and student_status is not None:
#             if student_status is not  None:
#                 queryset = queryset.filter(
# student__identification=identification, student__student_status = student_status)
#             else:
#                 queryset = queryset.filter(student__identification=identification)
#
#         elif student_status is not  None:
#             queryset = queryset.filter(students__student_status = student_status)
#             return queryset
#
#         # for temp in queryset:
#         # #     print("all", temp.student.name)
#         # #     temp.student.name = "pepe"
#         # #     print(temp.student.name)
#         #     temp.hash= temp.student.name
#         #print(temp.yearee)
#         return queryset


# TODO: URL TERMINADA
class SearchStudentViewSet(generics.ListAPIView):
    """Return all Groups2Students 1"""

    serializer_class = legacy_serializers.StudentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned faculty to a career,
        by filtering against a `years` query parameter in the URL.
        """
        queryset = Student.objects.using("sigenu_student").all()
        identification = self.request.query_params.get("identification")
        student_status = self.request.query_params.get("student_status")
        if identification is not None:
            if student_status is not None:
                queryset = queryset.filter(
                    identification=identification, student_status=student_status
                )
            else:
                queryset = queryset.filter(identification=identification)

        elif student_status is not None:
            queryset = queryset.filter(student_status=student_status)
            return queryset
        return queryset


class GenerateHashViewSet(generics.ListAPIView):
    """Return all Groups2Students 1"""

    serializer_class = legacy_serializers.StudentHashSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned faculty to a career,
        by filtering against a `years` query parameter in the URL.
        """
        queryset = StudentHash.objects.using("sigenu_student").all()

        return queryset


class Groups2StudentsOneViewSet(generics.ListAPIView):
    """Return all Groups2Students 1"""

    serializer_class = legacy_serializers.Groups2StudentsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned faculty to a career,
        by filtering against a `years` query parameter in the URL.
        """
        queryset = Groups2Students.objects.using("sigenu_student").filter(
            consecutive="0", students_fk__student_status="02", groups_fk__year="1"
        )
        career = self.request.query_params.get("career")
        faculty = self.request.query_params.get("faculty")
        if career is not None:
            if faculty is not None:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career,
                    students_fk__faculty__name=faculty,
                )
            else:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career
                )

        elif faculty is not None:
            queryset = queryset.filter(students_fk__faculty__name=faculty)
            return queryset
        return queryset


class Groups2StudentsTwoViewSet(generics.ListAPIView):
    """Return all Groups2Students 2"""

    serializer_class = legacy_serializers.Groups2StudentsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned faculty to a career,
        by filtering against a `years` query parameter in the URL.
        """
        queryset = Groups2Students.objects.using("sigenu_student").filter(
            consecutive="0", students_fk__student_status="02", groups_fk__year="2"
        )
        career = self.request.query_params.get("career")
        faculty = self.request.query_params.get("faculty")
        if career is not None:
            if faculty is not None:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career,
                    students_fk__faculty__name=faculty,
                )
            else:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career
                )

        elif faculty is not None:
            queryset = queryset.filter(students_fk__faculty__name=faculty)
            return queryset
        return queryset


class Groups2StudentsThreeViewSet(generics.ListAPIView):
    """Return all Groups2Students 3"""

    serializer_class = legacy_serializers.Groups2StudentsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned faculty to a career,
        by filtering against a `years` query parameter in the URL.
        """
        queryset = Groups2Students.objects.using("sigenu_student").filter(
            consecutive="0", students_fk__student_status="02", groups_fk__year="3"
        )
        career = self.request.query_params.get("career")
        faculty = self.request.query_params.get("faculty")
        if career is not None:
            if faculty is not None:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career,
                    students_fk__faculty__name=faculty,
                )
            else:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career
                )

        elif faculty is not None:
            queryset = queryset.filter(students_fk__faculty__name=faculty)
            return queryset
        return queryset


class Groups2StudentsFourViewSet(generics.ListAPIView):
    """Return all Groups2Students 4"""

    serializer_class = legacy_serializers.Groups2StudentsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned faculty to a career,
        by filtering against a `years` query parameter in the URL.
        """
        queryset = Groups2Students.objects.using("sigenu_student").filter(
            consecutive="0", students_fk__student_status="02", groups_fk__year="4"
        )
        career = self.request.query_params.get("career")
        faculty = self.request.query_params.get("faculty")
        if career is not None:
            if faculty is not None:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career,
                    students_fk__faculty__name=faculty,
                )
            else:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career
                )

        elif faculty is not None:
            queryset = queryset.filter(students_fk__faculty__name=faculty)
            return queryset
        return queryset


class Groups2StudentsFiveViewSet(generics.ListAPIView):
    """Return all Groups2Students 5"""

    serializer_class = legacy_serializers.Groups2StudentsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned faculty to a career,
        by filtering against a `years` query parameter in the URL.
        """
        queryset = Groups2Students.objects.using("sigenu_student").filter(
            consecutive="0", students_fk__student_status="02", groups_fk__year="5"
        )
        career = self.request.query_params.get("career")
        faculty = self.request.query_params.get("faculty")
        if career is not None:
            if faculty is not None:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career,
                    students_fk__faculty__name=faculty,
                )
            else:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career
                )

        elif faculty is not None:
            queryset = queryset.filter(students_fk__faculty__name=faculty)
            return queryset
        return queryset


class Groups2StudentsSixViewSet(generics.ListAPIView):
    """Return all Groups2Students 6"""

    serializer_class = legacy_serializers.Groups2StudentsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned faculty to a career,
        by filtering against a `years` query parameter in the URL.
        """
        queryset = Groups2Students.objects.using("sigenu_student").filter(
            consecutive="0", students_fk__student_status="02", groups_fk__year="6"
        )
        career = self.request.query_params.get("career")
        faculty = self.request.query_params.get("faculty")
        if career is not None:
            if faculty is not None:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career,
                    students_fk__faculty__name=faculty,
                )
            else:
                queryset = queryset.filter(
                    students_fk__career__national_career__name=career
                )

        elif faculty is not None:
            queryset = queryset.filter(students_fk__faculty__name=faculty)
            return queryset
        return queryset


@csrf_exempt
def student_dni(request, ci):
    """Returns the active employee given a CI"""
    # 92082643541
    try:
        student = Student.objects.using("sigenu_student").filter(identification=str(ci))
        # print(ci)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = legacy_serializers.StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        pass


def student_active_dni(request, ci):
    """Returns the active employee given a CI"""
    # 92082643541
    try:
        student = Student.objects.using("sigenu_student").filter(
            identification=str(ci), student_status="02"
        )
        # print(ci)

    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = legacy_serializers.StudentSerializer(student, many=True)
        # ///////////////////////////
        j = 0

        while j < len(serializer.data):
            # Select Givename
            if serializer.data[j]["name"]:
                givename = serializer.data[j]["name"]
                # print(serializer.data[j]["name"])
            else:
                givename = "None"
            # Select Middle_Name
            if serializer.data[j]["middle_name"]:
                middle_name = serializer.data[j]["middle_name"]
                # print(serializer.data[j]["middle_name"])
            else:
                middle_name = "None"
            # Select Last_Name
            if serializer.data[j]["last_name"]:
                last_name = serializer.data[j]["last_name"]
                # print(serializer.data[j]["last_name"])
            else:
                last_name = "None"

            # Select Country
            if serializer.data[j]["country"]:
                if serializer.data[j]["country"]["name"]:
                    country = serializer.data[j]["country"]["name"]
                    # print(serializer.data[j]["country"]["name"])
                else:
                    country = "None"
            else:
                country = "None"

            # Select Student_type
            if serializer.data[j]["student_type"]:
                if serializer.data[j]["student_type"]["kind"]:
                    student_type = serializer.data[j]["student_type"]["kind"]
                    # print(serializer.data[j]["student_type"]["kind"])
                else:
                    student_type = "None"
            else:
                student_type = "None"

            # Select Career
            if serializer.data[j]["career"]:
                if serializer.data[j]["career"]["national_career"]:
                    if serializer.data[j]["career"]["national_career"]["name"]:
                        career = serializer.data[j]["career"]["national_career"]["name"]
                        # print(serializer.data[j]["career"]["national_career"]["name"])
                    else:
                        career = "None"
                else:
                    career = "None"
            else:
                career = "None"

            # Select Faculty
            if serializer.data[j]["faculty"]:
                if serializer.data[j]["faculty"]["name"]:
                    faculty = serializer.data[j]["faculty"]["name"]
                    # print(serializer.data[j]["faculty"]["name"])
                else:
                    faculty = "None"
            else:
                faculty = "None"

            # Select Course_Type
            if serializer.data[j]["course_type"]:
                if serializer.data[j]["course_type"]["name"]:
                    course_type = serializer.data[j]["course_type"]["name"]
                    # print(serializer.data[j]["course_type"]["name"])
                else:
                    course_type = "None"
            else:
                course_type = "None"

            # Select scholastic_origin
            if serializer.data[j]["scholastic_origin"]:
                if serializer.data[j]["scholastic_origin"]["name"]:
                    cscholastic_origin = serializer.data[j]["scholastic_origin"]["name"]
                    # print(serializer.data[j]["scholastic_origin"]["name"])
                else:
                    cscholastic_origin = "None"
            else:
                cscholastic_origin = "None"

            # Select Town_university
            if serializer.data[j]["town_university"]:
                if serializer.data[j]["town_university"]["town"]:
                    if serializer.data[j]["town_university"]["town"]["name"]:
                        town_university = serializer.data[j]["town_university"]["town"][
                            "name"
                        ]
                        # print(serializer.data[j]["town_university"]["town"]["name"])
                    else:
                        town_university = "None"
                else:
                    town_university = "None"
            else:
                town_university = "None"

            # Select Matriculation_end_date
            if serializer.data[j]["faculty"]:
                if serializer.data[j]["faculty"]["university"]:
                    if serializer.data[j]["faculty"]["university"][
                        "matriculation_end_date"
                    ]:
                        matriculation_end_date = serializer.data[j]["faculty"][
                            "university"
                        ]["matriculation_end_date"]
                        # print(
                        #     serializer.data[j]["faculty"]["university"][
                        #         "matriculation_end_date"
                        #     ]
                        # )
                    else:
                        matriculation_end_date = "None"
                else:
                    matriculation_end_date = "None"
            else:
                matriculation_end_date = "None"

            # Select Rematriculation_end_date
            if serializer.data[j]["faculty"]:
                if serializer.data[j]["faculty"]["university"]:
                    if serializer.data[j]["faculty"]["university"][
                        "rematriculation_end_date"
                    ]:
                        rematriculation_end_date = serializer.data[j]["faculty"][
                            "university"
                        ]["rematriculation_end_date"]
                        # print(
                        #     serializer.data[j]["faculty"]["university"][
                        #         "rematriculation_end_date"
                        #     ]
                        # )
                    else:
                        rematriculation_end_date = "None"
                else:
                    rematriculation_end_date = "None"
            else:
                rematriculation_end_date = "None"

            ######################################

            # id_student = serializer.data[j]["id_student"]
            # print("IDE STUDENT", id_student)

            # groups2students = Groups2Students.objects.using("sigenu_student").filter(
            #     students_fk=id_student
            # )
            # serializer_group2student = legacy_serializers.Groups2StudentsSerializer(
            #     groups2students, many=True
            # )

            # print("TAMANO", len(serializer_group2student.data))

            # k = 0
            # groupm = 0

            # while k < len(serializer_group2student.data):
            #     if serializer_group2student.data[k]["consecutive"] == 0:
            #         # print("instance student", k, serializer_group2student.data[k])
            #         groupm = serializer_group2student.data[k]["groups_fk"]
            #         # print("groupfk------t", k, groupm)
            #     k = k + 1

            # xgroup = Xgroup.objects.using("sigenu_student").filter(id_group=groupm)
            # serializer_xgroup = legacy_serializers.XgroupSerializer(xgroup, many=True)

            # print("XXXXXXXXXXX", len(serializer_xgroup.data))

            # print("anno", serializer_xgroup.data)

            # year = str(serializer_xgroup.data[0]['year'])

            ########################################
            year = ""

            ###############

            hash = (
                givename
                + middle_name
                + last_name
                + country
                + student_type
                + career
                + faculty
                + course_type
                + cscholastic_origin
                + town_university
                + matriculation_end_date
                + rematriculation_end_date
            )

            hash_mod = hash.replace(
                " ", ""
            )  # elimina los espacios de la cadena de caracteres
            # print(hashlib.md5(hash_mod.encode("utf-8")).hexdigest())

            serializer.data[j]["hash_mod"] = hashlib.md5(
                hash_mod.encode("utf-8")
            ).hexdigest()
            serializer.data[j]["year"] = year

            j = j + 1

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        pass


@csrf_exempt
def student_active_name_full(request, name):
    """Returns the active student given a Name"""
    # 92082643541
    try:
        # students = Student.objects.using("sigenu_student").
        # filter(name__contains=str(name), student_status="02")
        # a = str(name).split(" ")[1]
        # print(a)
        students = Student.objects.using("sigenu_student").filter(
            name__contains=str(name), student_status="02"
        )

    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = legacy_serializers.StudentSerializerLinked(students, many=True)

        j = 0
        while j < len(serializer.data):
            id = serializer.data[j]["identification"]
            serializer.data[j]["uri"] = (
                str(request.build_absolute_uri().split("student_active_name_full")[0])
                + "student_active_dni/"
                + id
            )
            j = j + 1

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        pass


# import django_filters.rest_framework
# from django.contrib.auth.models import User

# from django_filters.rest_framework import DjangoFilterBackend


class ActivosList(generics.ListAPIView):
    # serializer_class = StudentSerializer
    serializer_class = legacy_serializers.StudentSerializerLinked
    queryset = Student.objects.using("sigenu_student").filter(student_status="02")
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "middle_name", "last_name"]

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     return Student.objects.using("sigenu_student").filter(student_status="02")


def game(request):
    faculty = Faculty.objects.using("sigenu_student").all()
    serializer = legacy_serializers.FacultySerializer(faculty, many=True)

    # regalos = ["pelota", "lazo", "veinte"]
    renos = ["fulanito", "menganito"]
    cantidad = []

    for tamanno in renos:
        cantidad.append(tamanno.__len__() * 2)
    # print(cantidad)

    return JsonResponse(serializer.data, safe=False)

    #
    # class ProductList(generics.ListCreateAPIView):
    #     queryset = Student.objects.all()
    #     serializer_class = StudentSerializer
    #     name = 'student-list'
    #
    #     filter_fields = (
    #         'name',
    #         'middle_name',
    #     )
