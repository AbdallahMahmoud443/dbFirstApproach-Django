from django.shortcuts import render

from dbfirstapproachapp.models import Categories

# Create your views here.



def ShowCategories(request):
    categories = Categories.objects.all();
    return render(request,'dbfirstapproach/showcategories.html',{'categories':categories})