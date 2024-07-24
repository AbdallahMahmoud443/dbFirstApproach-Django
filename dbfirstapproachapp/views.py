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

#* is efficient way  using procedures
def StoreProceduresDemo(request):
    grandTotal = 0
    runningTotal = 0
    runningOrderTotal = 0
    subtotal = 0
    
    # procedureName ='USP_GetAllOrders'
    conn = Connection()
    cursor = conn.cursor()
    cursor.execute("{call USP_GetAllOrders}")
    orders = cursor.fetchall()
    
    # Calculate runningTotal,runningOrderTotal,grandTotal and Generate Three new Columns
    newOrders =[]
    # related with runningOrderTotal calculate
    previousOrderID =0
    for order in orders:
        
        grandTotal += order.BillAmount
        runningTotal += order.BillAmount

        # calculate runningOrderTotal
        if previousOrderID == 0: 
            previousOrderID = order.OrderID      
            runningOrderTotal += order.BillAmount
            subtotal +=order.BillAmount 
                 
        elif previousOrderID == order.OrderID:
             runningOrderTotal += order.BillAmount
             subtotal +=order.BillAmount
        else:
            newOrders.append(GenerateNewOrder(0,subtotal,0)) # To Calculate subTotal
            previousOrderID = order.OrderID
            runningOrderTotal = order.BillAmount
            subtotal +=order.BillAmount 
            
        newOrders.append(GenerateNewOrder(order,runningTotal,runningOrderTotal))
        
    newOrders.append(GenerateNewOrder(0,subtotal,0))   # subtotal for last order
    return render(request,'dbfirstapproach/showorders.html',{'orders':newOrders,'grandTotal':grandTotal}) 

# Used To Generate order data in addition to two columns (runningTotal,runningOrderTotal)
def GenerateNewOrder (order,runningTotal,runningOrderTotal):
    if (order ==0):
          newOrder = {
            "OrderID":'',
            "OrderDate":'',
            "CompanyName":'',
            "ProductName":'',
            "UnitPrice":'',
            "Quantity":'',
            "BillAmount":'',
            "RunningTotal":runningTotal,
            "RunningOrderTotal":''
        }
    else:
        newOrder = {
            "OrderID":order.OrderID,
            "OrderDate":order.OrderDate,
            "CompanyName":order.CompanyName,
            "ProductName":order.ProductName,
            "UnitPrice":order.UnitPrice,
            "Quantity":order.Quantity,
            "BillAmount":order.BillAmount,
            "RunningTotal":runningTotal,
            "RunningOrderTotal":runningOrderTotal
        }
    return newOrder

  
def SPWithOutputParameter(request):
    # procedureName ='USP_GetAllOrders'
    conn = Connection()
    cursor = conn.cursor()
    # fetch total number of orders with procedures with output parameter
    count=0
    cursor.execute("{call USP_GetOrdersCount(?)}",count)
    counts = cursor.fetchval()
    # # fetch All orders with procedure
    cursor.execute("{call USP_GetAllOrders}") # output parameter => count
    orders = cursor.fetchall()
    
    return render(request,'dbfirstapproach/showorders.html',{'orders':orders,'counts':counts}) 

# Connection to Database by pyodbc
def Connection():
    
    ''' Related With Database Connection'''
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;Server=KINGDOMTECH;Database=northwind;Trusted_Connection=Yes;')
    return (conn)

