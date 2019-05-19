from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, 'index/index.html', {
        'nav_active': 'index'
    })


def portfolio(req):
    return render(req, 'portfolio/side_projects.html', {
        'nav_active': 'portfolio'
    })


def learning(req):
    return render(req, 'portfolio/continuous_learning.html', {
        'nav_active': 'learning'
    })


def blog(req):
    return render(req, 'blog/index.html', {
        'nav_active': 'blog'
    })
