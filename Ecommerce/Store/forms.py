#from django.forms import ModelForm
from Store.models import Additem,Itemlist
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Addform(forms.ModelForm):
	class Meta:
		model = Additem
		fields = ["Itname","price","itimg"] 
		widgets = {
		"Itname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter item name",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter item price",
			}),
		}

class ItemsForm(forms.ModelForm):
	class Meta:
		model = Itemlist
		fields = ["iname","price","itavailability","iimage"]
		widgets = {
		"iname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter Itemname",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Price",
			}),
		"itavailability":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter  Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter Username",
			}),
		}
