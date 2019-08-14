from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from coreManagerEmployees import views


urlpatterns = [
    path('',views.ApiRoot.as_view()),
    path('departaments/', views.DepartamentsViewSet.as_view()),
    path('employees/list/', views.EmployeeViewSet.as_view()),
    path('employees/update/<int:pk>', views.EmployeeUpdateViewSet.as_view()),
    path('employees/detail/<int:pk>', views.EmployeeDetailViewSet.as_view()),
    path('employees/create/', views.EmployeeCreateViewSet.as_view()),
    path('employees/delete/<int:pk>', views.EmployeeDeleteViewSet.as_view())
]

