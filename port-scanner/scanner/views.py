from django.shortcuts import render, redirect
from scanner.models import IP
import subprocess
import time


DB_NAME = '../db.sqlite3'

def index(request):
    ip = request.GET.get("ip")
    if ip is not None:
        subprocess.Popen(f'python ./scanner/scan_one.py {ip}')
        time.sleep(2)
        response = redirect('/')
        return response
    ip_objects = IP.objects.all().order_by('company')
    context = {
        'ips': ip_objects,
    }
    return render(request, 'index.html', context)
