from django.urls import path
from . import views

urlpatterns = [
    path('showcategories',views.ShowCategories,name="CategoriesPage"),
    path('orderlist',views.GetEmployeeBasedOnRawQuery,name="OrderListPage"),
    path('orderlistprocedure',views.StoreProceduresDemo,name="OrderListProcedurePage"),
    path('spwithoutputparameter',views.SPWithOutputParameter,name="SPWithOutputParameterPage"),
    path('filteringdemo',views.FilteringQuerySetsDemo,name="FilteringDemoPage"),
    path('accordoindemo',views.AccordoinDemo,name="AccordoinDemoPage"),
    path('mlaccordoindemo',views.MutiLevelAccordoinDemo,name="MLAccordoinDemoPage"),
    path('ordersusingtamplatetag',views.ShowOrdersUsingTamplateTag,name="OrdersUsingTamplateTagPage"),
    path('cachingdemo',views.CachingDemo,name="CachingDemoPage"),
    path('cachingdemo',views.CachingDemo,name="CachingDemoPage"),
    path('exporttocsv',views.ExportToCsv,name="export_to_csv"),
    path('exporttojson',views.ExportToJson,name="export_to_json"),
    path('exporttoexcel',views.ExportToExcel,name="export_to_excel"),
    path('exporttoword',views.ExportToWord,name="export_to_word"),
    path('exporttoedf',views.ExportToPDF,name="export_to_pdf"),
]
