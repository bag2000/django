from django.shortcuts import render
from scanner.models import IP, Company


def index(request):

        ip_objects = IP.objects.all().order_by('company')
        context = {
            'ips': ip_objects,
        }
        return render(request, 'index.html', context)
