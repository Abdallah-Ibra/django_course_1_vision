# import Http Response from django
from django.shortcuts import render
from home.models import Hero


# create a function
def heros_view(request):
	data = Hero.objects.all()
	context = {
		'students':data,
	}
	return render(request, "heros.html",context)