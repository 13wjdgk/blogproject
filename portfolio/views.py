from django.shortcuts import render

# Create your views here.
def portfoil (request):
    return render(request,'portfolio/portfolio.html')