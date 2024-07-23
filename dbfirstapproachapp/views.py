from django.shortcuts import render

from dbfirstapproachapp.models import Categories
import pyodbc
# Create your views here.

def ShowCategories(request):
    categories = Categories.objects.all();
    return render(request,'dbfirstapproach/showcategories.html',{'categories':categories})

def GetEmployeeBasedOnRawQuery(request):
    sql_query ='''
    SELECT a.OrderID,a.OrderDate,b.CompanyName,c.ProductName,d.UnitPrice,d.Quantity,d.UnitPrice * d.Quantity as 'BillAmount' 
    from Orders a inner join [Order Details] d on a.orderID = d.OrderID 
    inner join Customers b on a.CustomerID=b.CustomerID  inner join  Products c on d.ProductID =c.ProductID where a.OrderID between 10248 and 10255'''
    conn = Connection()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    orders = cursor.fetchall()
  
    return render(request,'dbfirstapproach/showorders.html',{'orders':orders})
    

def Connection():
    ''' Related With Database Connection'''
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;Server=KINGDOMTECH;Database=northwind;Trusted_Connection=Yes;')
    return (conn)