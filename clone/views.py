from django.shortcuts import render,redirect
from clone.forms import SignupForm
from clone.models import SignupModel

# Create your views here.

#index page
def index(request):
    return render(request,"index.html")

# for loginpage
def loginview(request):
    if request.method== "POST":
        print(request.POST)
        if SignupModel.objects.filter(signemail=request.POST['logemail']).exists():
            sign=SignupModel.objects.get(signemail=request.POST['logemail'])
            if sign.signpass==request.POST["logpass"]:
                return redirect('home')
            else:
                return redirect("home")
    return render(request,"login.html")

# for signup
def signupview(request):
    if request.method == "POST":
        print(request.POST)
        form=SignupForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect("login")  
        else:
            return render(request,"signup.html")
    return render(request,"signup.html")

#subcription page
def subspage(request):
    return render(request,"subscription.html")

#homepage
def home(request):
    return render(request,"home.html")

#movie description
def moviedesc(request):
    return render(request,"moviedesc.html")


#for user profile
def user(request):
    return render(request,"userprofile.html")