from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import GalleryForm
from .models import Gallery

User = get_user_model()

@login_required
def gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            image = form.cleaned_data['image']
            email = form.cleaned_data['tags']
            form.save()
            return redirect('base.html')
        return render(request, 'base.html', {'form': form})
    form =GalleryForm()
    return render(request, 'base.html', {'form': form})

