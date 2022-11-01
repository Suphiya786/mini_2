from django.urls import path
from . import apps
from . import views
urlpatterns =[
      path("",views.active,name="index"),
      path("index", views.index, name="index"),
      path("login",views.login_view,name="login"),
      path("register",views.register,name="register"),
      path("logout",views.logout_view,name="logout"),
      path("home",views.homepage,name="homepage"),
      path("notes",views.fnotes,name="notes"),
      path("about",views.about,name="about"),
      path("contact",views.contact,name="contact"),
      path(r'^create/',views.create,name="create"),
      path("create_pwd", views.create_pwd, name= "create_pwd"),
      path("retrieve", views.retrieve, name="retrieve"),
      path("decrypter/<int:id>", views.decrypter, name="decrypter"),
      path("nlogin",views.nlogin,name="nlogin"),
      path("blogin",views.blogin,name="blogin"),
      path("show/<int:id>",views.fshow,name="show"),
      path("pshow/<int:id>",views.pshow,name="pshow"),
      path("remnotes/<int:id>",views.remnotes,name="remnotes"),
      path("rempassword/<int:id>",views.rempassword,name="rempassword"),
]