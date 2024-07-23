from django.urls import path
from . import views

urlpatterns = [
    path('showcategories',views.ShowCategories,name="CategoriesPage"),
    path('orderlist',views.GetEmployeeBasedOnRawQuery,name="OrderListPage"),
     path('orderlistprocedure',views.StoreProceduresDemo,name="OrderListProcedurePage"),
    path('spwithoutputparameter',views.SPWithOutputParameter,name="SPWithOutputParameterPage"),
]
