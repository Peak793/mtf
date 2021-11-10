from django.shortcuts import render

# Create your views here.
def store(request):
     context = {}
     return render(request, 'store/store.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

def checkout(request):
     context = {}
     return render(request, 'store/checkout.html', context)

def fff(request):
     context = {}
     return render(request, 'store/fff.html', context)
def shirt(request):
     context = {}
     return render(request, 'store/shirt.html', context)

def jens(request):
     context = {}
     return render(request, 'store/jens.html', context)

def pong(request):
     context = {}
     return render(request, 'store/pong.html', context)

def shose(request):
     context = {}
     return render(request, 'store/shose.html', context)


def acc(request):
     context = {}
     return render(request,'store/acc.html', context)

