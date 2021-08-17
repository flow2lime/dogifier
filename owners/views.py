from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class DogifierView(View):
    def post(self, request):
        data = json.loads(request.body)
        