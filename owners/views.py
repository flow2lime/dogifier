from django.shortcuts import render
import json

from django.http import JsonResponse, HttpResponse
from django.views import View

from owners.models import Owner, Dog

class DogifierView(View):
    def post(self, request):
        data  = json.loads(request.body)

        def create_owner():
            Owner.objects.create(
                name  = data['owner_name'],
                email = data['owner_email'], 
                age   = data['owner_age']
            )
        
        def create_dog():
            Dog.objects.create(
                name  = data['dog_name'],
                age   = data['dog_age'],
                owner_id = data['dog_owner_id']
            )

            """Owner Check"""
        if 'owner' in data:
            try:
                if Owner.objects.filter(name=data['owner_name']).exists():
                    owner = Owner.objects.get(name=data['owner_name'])

                    if data['owner_email'] == owner.email and data['age'] == owner.age:
                        return JsonResponse({'message':'Registered owner!'}, status=422)
                    else:
                        create_owner()
                        return JsonResponse({'message':data}, status=201)
                else:
                    create_owner()
                    return JsonResponse({'message':data}, status=201)
            except:
                return JsonResponse({'message':'Error!!'}, status=400)

            """Dog Check""" 
        else:    
            try:
                if Dog.objects.filter(name=data['dog_name']).exists():
                    dog = Dog.objects.get(name=data['dog_name'])

                    if data['dog_age'] == dog.age and data['dog_owner_id'] == dog.owner_id:
                        return JsonResponse({'message':'Registered dog!'}, status=422)
                    else:
                        create_dog()
                        return JsonResponse({'message':data}, status=201)
                else:
                    create_dog()
                    return JsonResponse({'message':data}, status=201)
            except:
                return json({'message':'Error!!'}, status=400)
        