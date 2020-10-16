from django.shortcuts import render, redirect 
from .forms import *
from .models import Image
import datetime



def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'testapp/testapp.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'testapp/testapp.html', {'form': form})


    def readyToDownload(request):
        image = Image.objects.order_by('id')
        # download = datetime.datetime.now()
        # download_time = str(download)
        context = {
            'image': image
        }
        return render(request, 'testapp/success.html', context)

