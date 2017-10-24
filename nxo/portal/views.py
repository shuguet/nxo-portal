from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .upload import FileUpload
from .transform import extract_vms

def index(request):
    return HttpResponse("Hello, world. You're at the portal index.")


def upload(request):
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save()
            extract_vms(new_file)
            return HttpResponse('file uploaded')
    else:
        form = FileUpload()
    return render(request, 'upload.html', {
        'form': form
    })

