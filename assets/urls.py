from django.urls import include, path
from rest_framework import routers

from assets import views

###############

################


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'employee', views.EmployeeViewSet)

router.register(
    r"department_employee", views.DepartmentViewSet, basename="department_employee"
)
router.register(
    r"department_employee_linked",
    views.DepartmentLinkedViewSet,
    basename="department_employee_linked",
)
router.register(r"department", views.DepartmentTo)


router.register(r"employee_all", views.EmployeeAllViewSet, basename="employee_all")
router.register(
    r"employee_active_all", views.EmployeeActiveViewSet, basename="employee_active_all"
)


router.register(r"area", views.AreaViewSet, basename="area")
router.register(
    r"area_department", views.AreaEmployeeDepartmentViewSet, basename="area_department"
)

router.register(r"category", views.CategoryViewSet, basename="category")

router.register(r"position", views.PositionViewSet, basename="position")

router.register(r"profession", views.ProfessionViewSet, basename="profession")

router.register(r"specialty", views.SpecialtyViewSet, basename="specialty")

# router.register(r'employee_active_dni', views.UserViewSet, basename='AAAAAA')

router.get_api_root_view().cls.__name__ = "Raiz del Api Assets"

router.get_api_root_view().cls.__doc__ = (
    "{employee_active_name_full : http://localhost:port/"
    "employee_active_name_full/NomBr SegNom} \n"
    "--------------"
)


router.register(
    r"employee_custom", views.EmployeeCustomViewSet, basename="employe_custom"
)


urlpatterns = [
    # path('/api-auth/', include('rest_framework.urls')),
    path("", include(router.urls)),
    path("employee_active_dni/<str:ci>/", views.employees_active_dni),
    path("employee_all_dni/<str:ci>/", views.employee_get_dni),
    path("employee_active_name_full/<str:name>/", views.employee_active_name_full),
]
