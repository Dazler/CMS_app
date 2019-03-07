from django.shortcuts import render
from .forms import AircraftForm

# Create your views here.
def home(request):
  return render(request, 'CMS_app/index.html', {})

def A320(request):
	if(request.method=="POST"):
		form = AircraftForm()
		form = form.save(commit=False)
		form = AircraftForm(request.POST)
		form.ft = "A320"
		form.save()
	else:
		form = AircraftForm()
	return render(request, 'CMS_app/a320.html', {'form': form})

def A330(request):
	if(request.method=="POST"):
		form = AircraftForm()
		form = form.save(commit=False)
		form = AircraftForm(request.POST)
		form.ft = "A330"
		form.save()
	else:
		form = AircraftForm()
	return render(request, 'CMS_app/a330.html', {'form': form})

def A350(request):
	if(request.method=="POST"):
		form = AircraftForm()
		form = form.save(commit=False)
		form = AircraftForm(request.POST)
		form.ft = "A350"
		form.save()
	else:
		form = AircraftForm()
	return render(request, 'CMS_app/a350.html', {'form': form})