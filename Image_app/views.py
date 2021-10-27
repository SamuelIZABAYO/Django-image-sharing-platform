from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ImageCreatedForm


@login_required
def image_create(request, template_name='images/image/create.html'):
    if request.method == 'POST':
        form = ImageCreatedForm(data=request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_item.get_absolute_url())

    else:
        form = ImageCreatedForm(data=request.GET)
    return render(request,
                  template_name,
                  {'section': 'image',
                   'form': form})
