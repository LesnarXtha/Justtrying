from django.shortcuts import render,redirect

from django.http import HttpResponse
from vege.seed import *
from django.core.mail import send_mail
from django.conf import settings
from .models import *

def home(request):
    # subject = "This email from django server"
    # message = "This is a test message from django server email"
    # from_email = settings.EMAIL_HOST_USER
    # recipient_list = ["sthasunand@gmail.com"]
    # send_mail(subject,message,from_email,recipient_list)
    # # seed_db(100)
    
    Cars.objects.create(car_name="BMW",speed=80)
    
    peoples = [
        {'name':'Sunand Shrestha','age':22,},
        {'name':'Pawan Haramkhor','age':16,},
        {'name':'Manash pumpussy','age':21,},
        {'name':'Milan bhadwa','age':17,},
        {'name':'Avas Duds','age':21,}
    ]
    text="""
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex repudiandae odit quidem voluptatem dignissimos optio numquam tempore magni itaque delectus alias exercitationem laboriosam atque et ipsa nesciunt omnis nemo explicabo, saepe iste expedita eum rem autem! Nobis commodi impedit, dolores accusantium, odio quae eveniet sequi, obcaecati nihil accusamus aliquam totam libero facere voluptatem natus dicta mollitia quia iusto quis unde saepe ea voluptate? Numquam iste laboriosam blanditiis dolores dolore voluptatum libero commodi quisquam quidem modi! Laborum, saepe eligendi quasi et tempore vitae dignissimos. Sint, maxime dignissimos obcaecati nesciunt quidem ea ullam tempora. Eos, error! Adipisci dolorem aliquam id officia nisi.
    """
    vegetable = ['Potato','Brocoli','Tomato']
    return render(request, "home/index.html",context = {'peoples':peoples,'text':text, 'vegetable': vegetable})

def contact(request):
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")