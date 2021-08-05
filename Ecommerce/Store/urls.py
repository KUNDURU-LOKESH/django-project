from django.urls import path
from Store import views
from django.contrib.auth import views as v

urlpatterns=[
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cntct/',views.contact,name="ct"),
	path('aditem/',views.additem,name="adt"),
	path('itup/<int:m>/',views.itup,name="itup"),
	path('itdel/<int:n>/',views.itdel,name="itd"),
	path('itview/<int:a>/',views.itvw,name="itvw"),
	path('ilist/',views.itlist,name="itl"),
	path('rg/',views.usrreg,name="reg"),
	path('login/',v.LoginView.as_view(template_name="app/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="app/logout.html"),name="log"),

]