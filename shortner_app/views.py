from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from shortner_app.models import UrlShort


def redirect_alias(request, alias):
    try:
        alias_url = UrlShort.objects.get(alias=alias)
        return redirect(alias_url.url)
    except UrlShort.DoesNotExist:
        raise Http404
