from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.employee_form, name='employee_insert'), #localhost, get y post req. para insertar operaciones
    path('<int:id>/', views.employee_form, name='employee_update'), #get y post req. para actualizar operaciones
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/',views.employee_list, name='employee_list') # get req. para recuperar y desplegar todos los registros
]