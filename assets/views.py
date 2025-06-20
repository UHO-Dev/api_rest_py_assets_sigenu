from hashlib import md5

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from assets.models import Employee
from assets import serializers

# from assets.models import Snippet, Employee, Department
from assets.models import (
    Area,
    Category,
    Department,
    Employee,
    Position,
    Profession,
    Specialty,
)

"""
Employee active = >>>>> {active= True and inactive = False}
"""


# ViewSets define the view behavior.
# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.using("rh").all()
#     serializer_class = serializers.EmployeeSerializer
#     #permission_classes = [permissions.IsAuthenticated]


class AreaEmployeeDepartmentViewSet(viewsets.ModelViewSet):
    """Devuelve el area con con los departamentos,llave de cada trabajador en el area"""

    queryset = Area.objects.using("rh").all()
    serializer_class = serializers.AreaEmployeeDepartmentSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.using("int").all()
    serializer_class = serializers.AreaSerializer


#############################################
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.using("rh").all()
    serializer_class = serializers.DepartmentSerializer


class DepartmentLinkedViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.using("rh").all()
    serializer_class = serializers.DepartmentSerializerLinked


class DepartmentTo(viewsets.ModelViewSet):
    queryset = Department.objects.using("rh").all()
    serializer_class = serializers.DepartmentToSerializer


class EmployeeAllViewSet(viewsets.ModelViewSet):
    """Return all employees, inactive and inactive"""

    queryset = Employee.objects.using("rh").all()
    serializer_class = serializers.EmployeeSerializer


class EmployeeActiveViewSet(viewsets.ModelViewSet):
    """Return only employees active=True and inactive=False"""

    queryset = Employee.objects.using("rh").all().filter(active=True, inactive=False)
    serializer_class = serializers.EmployeeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.using("rh").all()
    serializer_class = serializers.CategorySerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.using("rh").all()
    serializer_class = serializers.PositionSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.using("rh").all()
    serializer_class = serializers.ProfessionSerializer


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.using("rh").all()
    serializer_class = serializers.SpecialtySerializer


@csrf_exempt
def employees_active_dni(request, ci):
    """Returns the active employee given a CI"""
    # 92082643541
    try:
        employees = Employee.objects.using("rh").filter(
            cid=str(ci), active=True, inactive=False
        )

        # s = 'Hola mundo!'
        # print(md5(s.encode("utf-8")).hexdigest())

        # i = 0
        # while i < len(employees):
        #     print(employees[i])
        #     employees[i].hash_mod = 'NUVOOOOOOOO'
        #     i = i + 1

    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        # i = 0
        # while i < len(employees):
        #     print(employees[i])
        #     employees[i].hash_mod = 'NUVOOOOOOOO'
        #     i = i + 1
        serializer = serializers.EmployeeSerializer(employees, many=True)
        # attr = ["name", "surname1", "surname2"]
        j = 0
        # r = 0
        while j < len(serializer.data):
            # Select Givename
            if serializer.data[j]["name"]:
                givename = serializer.data[j]["name"]
                # print(serializer.data[j]["name"])
            else:
                givename = "None"
            # Select Surname1
            if serializer.data[j]["surname1"]:
                surname1 = serializer.data[j]["surname1"]
                # print(serializer.data[j]["surname1"])
            else:
                surname1 = "None"
            # Select Surname2
            if serializer.data[j]["surname2"]:
                surname2 = serializer.data[j]["surname2"]
                # print(serializer.data[j]["surname2"])
            else:
                surname2 = "None"
            # Select Area_Name
            if serializer.data[j]["area"]:
                if serializer.data[j]["area"]["name"]:
                    area_name = serializer.data[j]["area"]["name"]
                    # print(serializer.data[j]["area"]["name"])
                else:
                    area_name = "None"
            else:
                area_name = "None"

            # Select Department_Name
            if serializer.data[j]["department"]:
                if serializer.data[j]["department"]["name"]:
                    department_name = serializer.data[j]["department"]["name"]
                    # print(serializer.data[j]["department"]["name"])
                else:
                    department_name = "None"
            else:
                department_name = "None"

                # Select Category_Classification
            if serializer.data[j]["category"]:
                if serializer.data[j]["category"]["classification"]:
                    category_classification = serializer.data[j]["category"][
                        "classification"
                    ]
                    # print(serializer.data[j]["category"]["classification"])
                else:
                    category_classification = "None"
            else:
                category_classification = "None"

                # Select Category_Classification
            if serializer.data[j]["position"]:
                if serializer.data[j]["position"]["name"]:
                    position_name = serializer.data[j]["position"]["name"]
                    # print(serializer.data[j]["position"]["name"])
                else:
                    position_name = "None"
                # Position_Category_Name
                if serializer.data[j]["position"]["category_name"]:
                    position_category_name = serializer.data[j]["position"][
                        "category_name"
                    ]
                    # print(serializer.data[j]["position"]["category_name"])
                else:
                    position_category_name = "None"
                # Position_Name
                if serializer.data[j]["position"]["subcategory_name"]:
                    position_subcategory_name = serializer.data[j]["position"][
                        "subcategory_name"
                    ]
                    # print(serializer.data[j]["position"]["subcategory_name"])
                else:
                    position_subcategory_name = "None"

            else:
                position_name = "None"
                position_category_name = "None"
                position_subcategory_name = "None"

            # Select Profession_Name
            if serializer.data[j]["profession"]:
                if serializer.data[j]["profession"]["name"]:
                    profession_name = serializer.data[j]["profession"]["name"]
                    # print(serializer.data[j]["profession"]["name"])
                else:
                    profession_name = "None"
            else:
                profession_name = "None"

            hash = (
                givename
                + surname1
                + surname2
                + area_name
                + department_name
                + category_classification
                + position_name
                + position_category_name
                + position_subcategory_name
                + profession_name
            )

            hash_mod = hash.replace(
                " ", ""
            )  # elimina los espacios de la cadena de caracteres
            # print(md5(hash_mod.encode("utf-8")).hexdigest())

            serializer.data[j]["hash_mod"] = md5(hash_mod.encode("utf-8")).hexdigest()
            j = j + 1

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        pass


@csrf_exempt
def employee_get_dni(request, ci):
    """
    devuelve los empleados dado un Ci
    """
    try:
        employee = Employee.objects.using("rh").filter(cid=str(ci))
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = serializers.EmployeeSerializer(employee, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        pass
        ########################################


@csrf_exempt
def employee_active_name_full(request, name):
    """Returns the active employee given a Name"""
    # 92082643541
    try:
        employees = Employee.objects.using("rh").filter(
            name__contains=str(name), active=True, inactive=False
        )

    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = serializers.EmployeeSerializerLinked(employees, many=True)

        j = 0
        while j < len(serializer.data):
            id = serializer.data[j]["cid"]
            serializer.data[j]["uri"] = (
                str(request.build_absolute_uri().split("employee_active_name_full")[0])
                + "employee_active_dni/"
                + id
            )
            j = j + 1

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        pass


class EmployeeCustomViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet custom.
    """

    queryset = Employee.objects.using("rh").all()
    serializer_class = serializers.EmployeeSerializer
    lookup_field = "pk"

    # ##Utilizo pk=None, utilizado en la funcin get_dni_all() como cid,
    #  para no modificar lookup_field####
    @action(detail=True)
    def get_dni_all(self, request, pk=None):
        """
        Returns a list of all the employees that have an identity card.
        """
        # user = self.get_object()
        # groups = user.groups.all()
        employee = Employee.objects.using("rh").filter(cid=str(pk))
        serializer = serializers.EmployeeSerializer(employee, many=True)

        # return Response([group.name for group in groups])
        return Response(serializer.data)
