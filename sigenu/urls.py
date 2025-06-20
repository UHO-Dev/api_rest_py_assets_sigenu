from django.urls import include, path
from rest_framework import routers

from sigenu import legacy_views, views

# Routers provide an easy way of automatically determining the URL conf.
legacy_router = routers.DefaultRouter()
# router.register(r'employee', views.EmployeeViewSet)
# router.register(r'department', views.DepartmentViewSet)
legacy_router.register(r"students", legacy_views.StudentAllViewSet)
legacy_router.register(r"students_active", legacy_views.StudentAllActiveViewSet)
legacy_router.register(r"country", legacy_views.CountryViewSet)
legacy_router.register(r"student_type", legacy_views.StudentTypeViewSet)
legacy_router.register(r"career", legacy_views.CareerViewSet)
legacy_router.register(r"entry_source", legacy_views.EntrySourceViewSet)
legacy_router.register(r"course_type", legacy_views.CourseTypeViewSet)
legacy_router.register(r"scholastic_origin", legacy_views.ScholasticOriginViewSet)
legacy_router.register(r"politic_org", legacy_views.PoliticOrgViewSet)
legacy_router.register(r"sex", legacy_views.SexViewSet)
legacy_router.register(r"town_university", legacy_views.TownUniversityViewSet)
legacy_router.register(r"marital_status", legacy_views.MaritalStatusViewSet)
legacy_router.register(r"study_regimen", legacy_views.StudyRegimenViewSet)
legacy_router.register(r"academic_situation", legacy_views.AcademicSituationViewSet)
legacy_router.register(r"town_situation", legacy_views.TownSituationViewSet)
legacy_router.register(r"skin_color", legacy_views.SkinColorViewSet)
legacy_router.register(r"student_status", legacy_views.StudentStatusViewSet)
legacy_router.register(r"faculty", legacy_views.FacultyViewSet)
legacy_router.register(r"orphan", legacy_views.OrphanViewSet)
legacy_router.register(r"study_program", legacy_views.StudyProgramViewSet)
legacy_router.register(r"xgroup", legacy_views.XgroupViewSet)
legacy_router.register(r"faculty_career", legacy_views.FacultyCareerViewSet)
# router.register(r'group2student_1', views.Groups2StudentsOneViewSet)
# router.register(r'group2student_2', views.Groups2StudentsTwoViewSet)
# router.register(r'group2student_3', views.Groups2StudentsThreeViewSet)
# router.register(r'group2student_4', views.Groups2StudentsFourViewSet)
# router.register(r'group2student_5', views.Groups2StudentsFiveViewSet)
# router.register(r'group2student_6', views.Groups2StudentsSixViewSet)


legacy_router.get_api_root_view().cls.__name__ = "Raiz del Api Sigenu"

legacy_router.get_api_root_view().cls.__doc__ = (
    "{student_active_name_full : http://localhost:port/"
    "student_active_name_full/NomBr SegNom} \n"
    "--------------"
)

urlpatterns_legacy = [
    # path('/api-auth/', include('rest_framework.urls')),
    path("", include(legacy_router.urls)),
    path("student_dni/<str:ci>/", legacy_views.student_dni),
    path("game/", legacy_views.game),
    path("student_active_dni/<str:ci>/", legacy_views.student_active_dni),
    path(
        "student_active_name_full/<str:name_full>/",
        legacy_views.student_active_name_full,
    ),
    path("search_active/", legacy_views.ActivosList.as_view()),
    path("group2student_1/", legacy_views.Groups2StudentsOneViewSet.as_view()),
    path("group2student_2/", legacy_views.Groups2StudentsTwoViewSet.as_view()),
    path("group2student_3/", legacy_views.Groups2StudentsThreeViewSet.as_view()),
    path("group2student_4/", legacy_views.Groups2StudentsFourViewSet.as_view()),
    path("group2student_5/", legacy_views.Groups2StudentsFiveViewSet.as_view()),
    path("group2student_6/", legacy_views.Groups2StudentsSixViewSet.as_view()),
    path("search/", legacy_views.SearchStudentViewSet.as_view()),
    path("hash/", legacy_views.GenerateHashViewSet.as_view()),
    # path('search_inactive', views.ActivosList.as_view()),#NO IMPLEMENTADO TODAVIA
    # path('search_all', views.ActivosList.as_view()),#NO IMPLEMENTADO TODAVIA
]


# #############################################################################
# ####         Above this is legacy code, kept only for reference         #####
# #############################################################################

router = routers.DefaultRouter()

router.register(r"students", views.StudentViewSet, "student-list")

urlpatterns = [
    path("", include(router.urls)),
]
urlpatterns += urlpatterns_legacy
