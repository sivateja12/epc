from django.urls import path,include
from . import views
urlpatterns = [
   # path("" ,views.IndexView,name="index"),
   #path("",views.htmlform,name="htmlform"),
   #path("",views.InsertPageView,name="insertpage"),
   #path("insert/",views.InsertData,name="insert"),
  
   #path("showpage/",views.ShowPage,name="showpage"),
   #path("editpage/<int:pk>",views.EditPage,name="editpage"),
   #path("update/<int:pk>",views.UpdateData,name="update"),
   #path("delete/<int:pk>",views.DeleteData,name="delete"),"""
  
   #path("",views.Register,name="registerpage"),
   path("",views.IndexPage,name="index"),
   path("signup/",views.SignupPage,name="signup"),
   path("register/",views.RegisterUser,name="register"),
   path("otppage/",views.OTPPage,name="otppage"),
   path("otp/",views.Otpverify,name="otp"),
   path("loginpage/",views.Loginpage,name="loginpage"),
   path("login/",views.LoginUser,name="login"),
   path("profile/",views.ProfilePage,name="profile"),
]
