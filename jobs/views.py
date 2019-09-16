from django.shortcuts import render, redirect
from faker import Faker

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def result(request):
    name = request.GET.get('name')
    fake = Faker('ko_KR')
    job = ''
    past_life
    return render(request,'jobs/result.html')