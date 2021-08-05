from django.shortcuts import render,redirect
from django.http import HttpResponse
from Store.forms import Addform,ItemsForm,UsgForm
from Store.models import Additem,Itemlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	w = Additem.objects.all()
	return render(request,'app/home.html',{'c':w})

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')
@login_required
def additem(request):
	y = Additem.objects.all()
	if request.method == "POST":
		t = Addform(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Item Added Successfully")
			return redirect('/aditem')
	t = Addform()
	return render(request,'app/additemlist.html',{'q':t,'a':y})


@login_required
def itup(request,m):
	k = Additem.objects.get(id=m)
	if request.method == "POST":
		e = Addform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Item updated Successfully".format(k.Itname))
			return redirect('/aditem')
	e = Addform(instance = k)
	return render(request,'app/itupdate.html',{'x':e})

@login_required
def itdel(request,n):
	v = Additem.objects.get(id=n)
	if request.method == "POST":
		messages.info(request,"{} Item Deleted Successfully".format(v.Itname))
		v.delete()
		return redirect('/aditem')
	return render(request,'app/itdelete.html',{'q':v})

@login_required
def itvw(request,a):
	s = Additem.objects.get(id=a)
	return render(request,'app/itview.html',{'z':s})

def itlist(request):
	m = Itemlist.objects.all
	if request.method =="POST":
		k = ItemsForm(request.POST,request.FILES)
		if k.is_valid():
			n = k.save(commit=False)
			messages.success(request,'{} Item is added Successfully'.format(n.iname))
			n.save()
			return redirect('/ilist')
	k = ItemsForm()
	return render(request,'app/itmlist.html',{'r':k,'s':m})


def usrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/rg')
	d = UsgForm()
	return render(request,'app/userregister.html',{'t':d})