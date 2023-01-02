from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Login
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, '<h2> You have successfully logged in!!! </h2>')
    return render(request, 'index.html')

def aboutus (request):
    return render(request, 'aboutus.html' )

def login (request):
    if request.method == "POST":
        login= Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        login.save()
        #return HttpResponse('<h2> You have successfully logged in!!! </h2>')
        return render(request, 'index.html')

    return render(request, 'login.html')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "login.html" 

def cart (request):
    return render(request, 'cart.html' )
    
    