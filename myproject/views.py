from django.shortcuts import render
from django.contrib.auth.models import User

def testview(request):
    return render(request, 'test.html', {'users': User.objects.all()})
