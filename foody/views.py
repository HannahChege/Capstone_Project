from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import food,Restaurant
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from random import choice
from .email import send_welcome_email

# Create your views here.
def foody (request):
    foods = food.objects.all()
    for fod in foods:
        fod.un = ''.join(choice('atrdsuhfdsefreh') for _ in range(10))
    return render(request,'food.html',{'foods':foods})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})
def search_results(request):

    if 'food' in request.GET and request.GET["food"]:
        search_term = request.GET.get("food")
        searched_foods = Food.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"foods": searched_foods})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})  

def food_today(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('food_today')
    else:
        form = SubscribeForm()
    return render(request, 'food.html', {"date": date,"foods":foods,"subscribeForm":form})