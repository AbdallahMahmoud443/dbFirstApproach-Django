from django.urls import path
from . import views

urlpatterns = [
    path('showcategories',views.ShowCategories,name="CategoriesPage"),
    path('orderlist',views.GetEmployeeBasedOnRawQuery,name="OrderListPage"),
]
