from django import template
from dbfirstapproachapp.models import Orders,OrderDetails


# Create Register 
register = template.Library()

# Create Custom Tag to Show Order and OrderDetials to Specific Range of Employees
@register.inclusion_tag('dbfirstapproach/accordoindemo_TT.html')
def show_orders(start=10248,end=10255):
 #* Logic tricky
    orders =Orders.objects.filter(orderid__range=[start,end]).order_by('orderid')
    orders_ids = [ order.orderid for order in orders] # ids for all orders
    orders_details = OrderDetails.objects.filter(orderid__in=orders_ids)
    # Then WE Need show orders,orders_details in spesific template tag
    dict ={'orders':orders,
           'orders_details':orders_details}
    
    return dict

