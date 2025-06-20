from django.db import models


class Area(models.Model):
    id = models.CharField(db_column="Id_Ccosto", primary_key=True, max_length=15)
    name = models.TextField(db_column="Desc_Ccosto")

    class Meta:
        managed = False
        db_table = "Centro_Costo"
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.CharField(db_column="Id_Direccion", primary_key=True, max_length=15)
    name = models.TextField(db_column="Desc_Direccion")

    class Meta:
        managed = False
        db_table = "RH_Unidades_Organizativas"
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return f"{self.id}: {self.name}"


class Category(models.Model):
    id = models.CharField(db_column="Id_Categoria_DI", max_length=5, primary_key=True)
    description = models.CharField(db_column="Desc_Categoria_DI", max_length=50)
    # identification_di = models.CharField(db_column='Identificacion_DI', max_length=2)
    classification = models.CharField(db_column="Clasificacion_DI", max_length=1)
    # years_di = models.SmallIntegerField(db_column='Anos_DI')

    class Meta:
        managed = False
        db_table = "RH_Categorias_Docente_Invest"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return " ".join([self.id]).strip()


class Position(models.Model):
    id = models.CharField(db_column="Id_Cargo", max_length=5, primary_key=True)
    name = models.CharField(db_column="Desc_Cargo", max_length=120)

    category_name = models.CharField(db_column="Desc_Categoria", max_length=25)
    subcategory_name = models.CharField(db_column="Desc_Subcategoria", max_length=50)

    basic_wage = models.DecimalField(
        db_column="Salario_Basico", max_digits=10, decimal_places=4
    )
    seniority = models.DecimalField(
        db_column="Antiguedad", max_digits=10, decimal_places=4
    )

    # rgrupo = models.CharField(db_column='RGrupo', max_length=5)
    # ngrupo = models.CharField(db_column='NGrupo', max_length=3)
    # id_categoria = models.CharField(db_column='Id_Categoria', max_length=5)
    # id_subcategoria = models.CharField(db_column='Id_Subcategoria', max_length=5)
    # resolucion = models.CharField(db_column='Resolucion', max_length=20)
    # clasificacion = models.CharField(db_column='Clasificacion', max_length=1)
    # porciento_simultaneidad = models.DecimalField(
    # db_column='Porciento_Simultaneidad', max_digits=19, decimal_places=6)
    # funcionario = models.BooleanField(db_column='Funcionario')
    # ejecutivo = models.BooleanField(db_column='Ejecutivo')
    # apoyo = models.BooleanField(db_column='Apoyo')
    # reportflag = models.BooleanField(db_column='ReportFlag')
    # coeficiente_multioficio = models.DecimalField(
    # db_column='Coeficiente_Multioficio', max_digits=19, decimal_places=6)
    # coeficente_empresa_empleadora = models.DecimalField(
    # db_column='Coeficente_Empresa_Empleadora', max_digits=8, decimal_places=2)
    # mscodgrupo = models.CharField(db_column='MSCodGrupo', max_length=3)
    # plus = models.DecimalField(db_column='Plus', max_digits=10, decimal_places=4)
    # salario_cargo = models.DecimalField(db_column='Salario_Cargo',
    #  max_digits=10, decimal_places=4)
    # estimulo = models.DecimalField(db_column='Estimulo', max_digits=10,
    # decimal_places=4)
    # otros = models.DecimalField(db_column='Otros', max_digits=10, decimal_places=4)
    # ieterritorial = models.DecimalField(db_column='IETerritorial',
    #  max_digits=5, decimal_places=2)
    # etsector = models.DecimalField(db_column='ETSector', max_digits=5,
    #  decimal_places=2)
    # otrasretribuciones = models.DecimalField(db_column='OtrasRetribuciones',
    #  max_digits=8, decimal_places=2)
    # horarioirregular = models.DecimalField(db_column='HorarioIrregular',
    #  max_digits=10, decimal_places=4)
    # otras_cla = models.DecimalField(db_column='Otras_CLA', max_digits=10,
    # decimal_places=4)
    # id_clasif_p2 = models.CharField(db_column='Id_Clasif_P2', max_length=3)

    class Meta:
        managed = False
        db_table = "RH_Cargos"
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return " ".join([self.id, self.name]).strip()


class Specialty(models.Model):
    id = models.CharField(db_column="Id_Especialidad", max_length=3, primary_key=True)
    name = models.CharField(db_column="Desc_Especialidad", max_length=25)

    class Meta:
        managed = False
        db_table = "RH_Profesiones_General"
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def __str__(self):
        return " ".join([self.id, self.name]).strip()


class Profession(models.Model):
    specialty = models.ForeignKey(
        "Specialty",
        db_column="Id_Especialidad",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    id = models.CharField(db_column="Id_Profesion", max_length=5, primary_key=True)
    name = models.CharField(db_column="Desc_Profesion", max_length=80)
    # id_especialidad = models.CharField(db_column='Id_Especialidad', max_length=3)

    class Meta:
        managed = False
        db_table = "RH_Profesiones"
        verbose_name = "Profession"
        verbose_name_plural = "Professions"

    def __str__(self):
        return " ".join([self.id, self.name]).strip()


class Employee(models.Model):
    id = models.CharField(db_column="Id_Empleado", primary_key=True, max_length=15)
    fid = models.CharField(db_column="Id_Expediente", max_length=15)
    cid = models.CharField(db_column="No_CI", max_length=15)

    name = models.TextField(db_column="Nombre")
    surname1 = models.TextField(db_column="Apellido_1")
    surname2 = models.TextField(db_column="Apellido_2")
    gender = models.CharField(db_column="Sexo", max_length=1)

    active = models.CharField(db_column="Alta", null=True, max_length=15)  # BOOL
    inactive = models.CharField(db_column="Baja", null=True, max_length=15)  # BOOL

    phone = models.TextField(db_column="Telefono_Particular")
    # area = models.ForeignKey(Area, related_name='employees_id_area',
    # db_column="Id_CCosto", blank=True, null=True, on_delete=models.CASCADE)
    area = models.ForeignKey(
        Area,
        related_name="employees_id_area",
        db_column="Id_CCosto",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    department = models.ForeignKey(
        Department,
        related_name="employees_id_department",
        db_column="Id_Direccion",
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        Category,
        db_column="Id_Categoria_DI",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    position = models.ForeignKey(
        Position, db_column="Id_Cargo", blank=True, null=True, on_delete=models.CASCADE
    )
    profession = models.ForeignKey(
        Profession,
        db_column="Id_Profesion",
        max_length=5,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    address = models.TextField(db_column="Direccion")
    city = models.TextField(db_column="Ciudad")
    region = models.TextField(db_column="Region")
    postal_code = models.TextField(db_column="Codigo_Postal")
    country = models.TextField(db_column="Pais")

    date_hired = models.TextField(db_column="Fecha_Contratacion")

    class Meta:
        managed = False
        db_table = "Empleados_Gral"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.fid}{self.name}{self.cid}"

    # def hash_mod(self):
    #     # chars = '%s%s%s' % (self.fid, self.name, self.cid)
    #     charsi = ''.join('%s%s%s' % (self.fid, self.name, self.cid)).replace(' ', '')
    #     return  charsi

    def hash_mod(self):
        return ""


class EmployeeDniKey(models.Model):
    cid = models.CharField(
        db_column="No_CI",
        max_length=15,
        primary_key=True,
    )
    department = models.ForeignKey(
        Department,
        related_name="employees_dni_department",
        db_column="Id_Direccion",
        on_delete=models.CASCADE,
    )

    class Meta:
        managed = False
        db_table = "Empleados_Gral"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return " ".join([self.cid]).strip()


class EmployeeDniArea(models.Model):
    id_direccion = models.CharField(
        db_column="Id_Direccion", max_length=15, primary_key=True
    )
    area = models.ForeignKey(
        Area,
        related_name="id_department",
        db_column="Id_CCosto",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        managed = False
        db_table = "Empleados_Gral"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return " ".join([self.id_direccion]).strip()
