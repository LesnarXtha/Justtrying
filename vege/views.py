from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

@login_required(login_url='/login/')
def recipes(request):
    if request.method == "POST":
    
        data = request.POST
        
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )
        
        return redirect('/recipes/')
    
    query_set = Recipe.objects.all()
    
    if request.GET.get('search'):
        query_set = query_set.filter(recipe_name__icontains = request.GET.get('search'))
    
    context = {'recipes':query_set}
    
    return render(request,'recipes.html',context)

@login_required(login_url='/login/')
def delete_recipe(request,id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')

@login_required(login_url='/login/')
def update_recipe(request,id):
    
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        
        if recipe_image: # If new image uploaded
            queryset.recipe_image = recipe_image
            
        queryset.save()
        return redirect('/recipes/')
        
    context = {'recipes':queryset}
    
    return render(request,'update_recipe.html',context)


def login_page(request):
    
    if request.method == "POST":
        
        data = request.POST
        
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.filter(username = username)
        
        if not user.exists():
            messages.error(request,'Invalid name')
            return redirect('/login/')
        
        user = authenticate(username = username,password = password )
        
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipes/')
    
    return render(request,'login.html')

def logout_page(request):
    
    logout(request)
    return redirect('/login/')

def register(request):
    
    if request.method == "POST":
        
        data = request.POST
        
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user_name = data.get('user_name')
        password = data.get('password')
        
        user = User.objects.filter(username = user_name)
        if user.exists():
            messages.info(request,"Name already existed Please Select Another Name")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=user_name
        )
        
        user.set_password(password)
        user.save()
        
        messages.info(request,"Account Created Successfully")
        return redirect('/register/')
    
    return render(request,'register.html')
 
 
@login_required(login_url='/login/')
def get_student(request):
    
    queryset = Student.objects.all()
    
    if request.GET.get('Search'):
        search = request.GET.get('Search')
        queryset = Student.objects.filter(
            Q(student_name__icontains = search)|
            Q(student_id__student_id__icontains = search)|
            Q(student_email__icontains = search)|
            Q(department__department__icontains = search)
        )
    
    if request.GET.get('reset'):
        queryset = Student.objects.all()

    
    paginator = Paginator(queryset, 8)  # Show 8 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    context ={'queryset':page_obj}
    return render(request,'report/student.html',context)

def see_marks(request,student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    ranks = Student.objects.annotate(marks = Sum('student_marks__marks')).order_by('-marks')
    current_rank = -1
    i = 1
    
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            current_rank = i
            break
        i += 1
    
    return render(request,'report/see_marks.html',{'queryset':queryset,'total_marks':total_marks,'current_rank':current_rank})
