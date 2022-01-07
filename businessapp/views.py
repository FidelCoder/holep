from django.db.models.fields import files
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Image
from django.core.mail import send_mail
from . form import ImageForm


# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'businessapp/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'businessapp/post_detail.html'

#class AboutDetail(generic.DetailView):
#    template_name = 'businessapp/aboutus.html'

def aboutus(request):
    return render(request, 'businessapp/aboutus.html')


def services(request):
    return render(request, 'businessapp/services.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['holepcompanyltd@gmail.com'])
        return render(request, 'businessapp/thankyou.html')
    return render(request, 'businessapp/contacts.html', {})


def homepage(request):
    return render(request, 'businessapp/homepage.html')


def thankyou(request):
    return render(request, 'businessapp/thankyou.html')

def contribuition(request):
    return render(request, 'businessapp/contribuition.html')



def Ourgallery(request):
    if request.method == 'POST':
        form = ImageForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'businessapp/gallery.html', {"obj":obj})

    else:
        form = ImageForm()
        img = Image.objects.all()
    return render(request, 'businessapp/gallery.html', {'img':img, 'form':form})


def trainingPrograme(request):
    return render(request, 'businessapp/trainingp.html')


def Values(request):
    return render(request, 'businessapp/changes.html')
