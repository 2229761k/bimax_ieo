from django.shortcuts import render, redirect, reverse


# Create your views here.

def post_list(request):
    return render(request, 'bimax_ieo/post_list.html', {})

def toka(request):
    return render(request, 'bimax_ieo/toka.html', {})

def gpa(request):
    return render(request, 'bimax_ieo/gpa.html', {})