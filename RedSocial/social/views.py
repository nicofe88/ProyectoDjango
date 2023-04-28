from django.shortcuts import render
from .Forms import UserRegister

# Create your views here.
def signup(request):
    if(request.method == 'POST'):
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegister()

    return render(request, 'signup.html', {'form': form})