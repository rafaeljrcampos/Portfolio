from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    produtos = Produto.objects.all()

    return render(request, 'home_index.html')