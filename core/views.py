from .models import  Company
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import newcompanyform


def home(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})

def company_desc(request, pk):
	try:
		company = Company.objects.get(pk=pk)
	except Company.DoesNotExist:
		raise Http404
	return render(request, 'description.html', {'company': company})




def index(request):
    company = Company.objects.order_by('id')
    form = newcompanyform()
    return render(request, 'newpost.html',{'index': company, 'form':form},)

def content_get(request):
    company = Company.objects.order_by('id')
    if request.method == 'POST':
        form=newcompanyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = newcompanyform()
    return render(request, 'newpost.html',{'index': company, 'form':form},)    
