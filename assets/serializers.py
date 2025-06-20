from rest_framework import serializers

# from assets.models import Employee, Department
from assets.models import (
    Area,
    Category,
    Department,
    Employee,
    Position,
    Profession,
    Specialty,
)


class AreaEmployeeDepartmentSerializer(serializers.ModelSerializer):
    # departments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ["id", "name", "id_department"]


class DepartmentSerializer(serializers.ModelSerializer):
    # departments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ["id", "name", "employees_id_department", "employees_dni_department"]


class DepartmentSerializerLinked(serializers.HyperlinkedModelSerializer):
    # departments = serializers.Hyperlink()

    class Meta:
        model = Department
        fields = ["id", "name", "employees_id_department"]


class DepartmentToSerializer(serializers.ModelSerializer):
    # departments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ["id", "name"]


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "description", "classification"]


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            "id",
            "name",
            "category_name",
            "subcategory_name",
            "basic_wage",
            "seniority",
        ]


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ["id", "name"]


class ProfessionSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()

    class Meta:
        model = Profession
        fields = ["id", "name", "specialty"]


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentToSerializer()
    area = AreaSerializer()
    category = CategorySerializer()
    position = PositionSerializer()
    profession = ProfessionSerializer()

    class Meta:
        model = Employee
        fields = [
            "id",
            "fid",
            "cid",
            "name",
            "surname1",
            "surname2",
            "gender",
            "active",
            "inactive",
            "phone",
            "area",
            "department",
            "category",
            "position",
            "profession",
            "address",
            "city",
            "region",
            "postal_code",
            "country",
            "date_hired",
            "hash_mod",
        ]


class EmployeeSerializerLinked(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "cid", "name"]
