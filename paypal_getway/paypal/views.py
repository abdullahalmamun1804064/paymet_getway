from django.shortcuts import render

# Create your views here.
def paypal(request):
    return render(request,'paypal/paypal.html')