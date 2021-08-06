from django.shortcuts import render
from home.models import Content, Glimpses
# Create your views here.


def home(request):
    data1, data2 = Content.objects.filter(category='Home')
    cards = Content.objects.filter(category='Card')
    corousel = Glimpses.objects.get(pk=4)
    images = corousel.images.all()
    return render(request, 'home/home.html', {'images': images, 'home1': data1, 'home2': data2, 'cards': cards})


def facilities(request):
    facilities = Content.objects.filter(category='Facilities')
    return render(request, 'home/facilities.html', {'facilities': facilities})


def contact(request):
    return render(request, 'home/contact.html')


def academic(request):
    academics = Content.objects.filter(category='Academic Details')
    return render(request, 'home/academic.html', {'academics': academics})


def admission(request):
    message = Content.objects.get(pk=4)
    return render(request, 'home/admission.html', {'data': message})


def about(request):
    message = Content.objects.get(pk=4)
    corousel = Glimpses.objects.get(pk=4)
    images = corousel.images.all()
    return render(request, 'home/about.html', {'data': message, 'images': images})


def principal(request):
    message = Content.objects.get(pk=1)
    return render(request, 'home/administrators.html', {'data': message})


def administrator(request):
    message = Content.objects.get(pk=2)
    return render(request, 'home/administrators.html', {'data': message})


def president(request):
    message = Content.objects.get(pk=3)
    return render(request, 'home/administrators.html', {'data': message})


def glimpses(request):
    # luckydraw images fetch
    luckydraw = Glimpses.objects.get(pk=1)
    luckydraw_image = luckydraw.images.all()
    # Pariksha Images fetch
    pariksha = Glimpses.objects.get(pk=2)
    pariksha_image = pariksha.images.all()
    # yoga day images fetch
    yogaday = Glimpses.objects.get(pk=3)
    yogaday_image = yogaday.images.all()
    return render(request, 'home/glimpses.html', {'luckydraw_image': luckydraw_image, 'pariksha_image': pariksha_image, 'yogaday_image': yogaday_image})
