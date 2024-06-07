from django.shortcuts import render,redirect
from .models import *
from random import randint
# Create your views here.
#def IndexView(request):
 #   return render(request,"jobapp/index.html")
#def htmlform(request):
  #  return render(request,"jobapp/Forms.html")

def IndexPage(request):
    return render(request,"jobapp/index.html")



def SignupPage(request):
    return render(request,"jobapp/signup.html")




def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already Exiat"
            return render(request,"jobapp/signup.html",{'msg':message})

        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"jobapp/otpverify.html",{'email':email})


    else:
        print("Company Registration")


def OTPPage(request):
    return render(request,"jobapp/otpverify.html")


def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)


    if user:
        if user.otp ==otp:
            message = "Otp verified successfully"
            return render(request,"jobapp/login.html",{'msg':message})
        else:
            message = "Incorrect otp"
            return render(request,"jobapp/otpverify.html",{'msg':message})

    else:
        return render(request,"jobapp/signup.html")



def Loginpage(request):
    return render(request,"jobapp/login.html")

def LoginUser(request):
    if request.POST['role']=='Candidate':
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                return redirect('index')

            else:
                message = "Password doesnot match"
                return render(request,"jobapp/login.html",{'msg':message})
    else:
        message = "User doesnot exist"
        return render(request,"jobapp/login.html",{'msg':message})




def ProfilePage(request):
   return render(request,'jobapp/profile.html')