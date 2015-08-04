from django.shortcuts import render

from .models import Entry
from .models import Project
from .models import Client


def entries(request):
    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
    })

def projects(request):
	project_list = Project.objects.all()
	return render(request, 'projects.html', {
		'project_list' : project_list,
	})

def clients(request):
	client_list = Client.objects.all()
	return render(request, 'clients.html', {
		'client_list' : client_list,
	})

def summary(request):
	summary_all = Entry.objects.all() 
	return render(request, 'summary.html', {
		"summary_all": summary_all,
		})