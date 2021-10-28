from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ImageCreatedForm
from .models import Image


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


def image_detail(request, id, slug,
                 template_name='images/image/image_detail.html'):
    single_image = Image.objects.get(id=id, slug=slug)
    context = {'single_image': single_image}
    return render(request, template_name, context)
