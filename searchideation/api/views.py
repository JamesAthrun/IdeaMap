from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

import json
import requests
import pprint

# Create your views here.

def main(request):
    return HttpResponse("Hello")

def getSearchResult(APIView):
    subscriptionKey = "cc0fb19845114c3c96090550aaf1b66f"
    customConfigId = "86883689-d776-42cf-bd01-2ce7b319a242"
    searchTerm = "creativity"

    url = 'https://api.bing.microsoft.com/v7.0/custom/search?' + 'q=' + searchTerm + '&' + 'customconfig=' + customConfigId
    r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
    pprint.pprint(r.text)