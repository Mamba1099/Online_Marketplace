from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.http import HttpResponseRedirect, QueryDict
from urllib.parse import urlparse, urlunparse
from item.models import Category, Item

from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })

def logout_then_login(request, login_url='login'):

    login_url = (settings.LOGIN_URL)
    return LogoutView.as_view(next_page=login_url)(request)

def redirect_to_login(next, redirect_field_name='logout'):
    """
    Redirect the user to the login page, passing the given 'next' page.
    """
    resolved_url = (settings.LOGIN_URL)

    login_url_parts = list(urlparse(resolved_url))
    if redirect_field_name:
        querystring = QueryDict(login_url_parts[4], mutable=True)
        querystring[redirect_field_name] = next
        login_url_parts[4] = querystring.urlencode(safe="/")

    return HttpResponseRedirect(urlunparse(login_url_parts))