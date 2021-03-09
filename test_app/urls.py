from django.urls import path,include
from rest_framework.routers import DefaultRouter
from test_app import views

router = DefaultRouter()

router.register('department', views.DepartmentApi, basename='department')
router.register('employee', views.EmployeeApi, basename='employee')



urlpatterns = [
    path('api/',include(router.urls)),
    path('api/function/department', views.departmentList, name='departments'),
    path('api/function/department/<int:pk>', views.departmentModify, name='departments_modify'),
    path('api/function/employee', views.employeeList, name='employee'),
    path('api/function/employee/<int:pk>', views.employeeModify, name='employeeedit'),

]