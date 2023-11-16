# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Secret
import uuid



def home(request):
    return render(request, 'home.html')


def create_secret(request):
    if request.method == 'POST':
        secret_text = request.POST.get('secret_text', '')
        unique_url = uuid.uuid4().hex[:6].upper()
        secret = Secret.objects.create(secret_text=secret_text, unique_url=unique_url)
        return render(request, 'secret_created.html', {'unique_url': request.get_host() + '/' + secret.unique_url})
    return render(request, 'create_secret.html')


def view_secret(request, unique_url):
    secret = get_object_or_404(Secret, unique_url=unique_url)

    if secret.views_remaining <= 0:
        raise Http404("This secret has already been viewed.")

    secret.views_remaining -= 1
    secret.save()

    return render(request, 'view_secret.html', {'secret_text': secret.secret_text})
