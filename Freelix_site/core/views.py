from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movies
from django.contrib.auth.decorators import login_required



def index(request):
   
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Crediatials are not valid !")
            return render (request, 'login.html')
    
    return render(request, 'login.html')

def signup(request):

    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username, email=email).exists():
            messages.info(request, "Already a user, Please Log in !")
            return redirect('login')
        
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email Already Registered !")
            return redirect("signup")
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username Already Registered !")
            return redirect("signup")

        
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            #To Log user in

            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)
            return redirect('home')

    else: 
        return render(request, 'signup.html')   

def home(request):
    
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def movies(request):
    movies = Movies.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies.html', context)


@login_required(login_url='login')
def movie_detail(request, pk):
    movie_uuid = pk
    movie_detail = Movies.objects.get(uu_id=movie_uuid)

    context = {
        'movie_detail': movie_detail
    }
    return render(request, 'movie_detail.html', context)
def tv(request):
    return render(request, 'tv.html')

@login_required(login_url='login')
def search(request):
    return render(request, 'search.html')
# Create your views here.
