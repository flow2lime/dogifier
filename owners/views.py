from django.shortcuts import render
import json

from django.http import JsonResponse, HttpResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerProfilerView(View):

    def post(self, request):
        data  = json.loads(request.body)

        def create_owner():
            Owner.objects.create(
                name  = data['owner_name'],
                email = data['owner_email'], 
                age   = data['owner_age']
            )

        try:
            if Owner.objects.filter(name=data['owner_name']).exists():
                owner = Owner.objects.get(name=data['owner_name'])

                if data['owner_email'] == owner.email and data['age'] == owner.age:
                    return JsonResponse({'message':'Registered owner!'}, status=409)
                else:
                    create_owner()
                    return JsonResponse({'message':data}, status=201)
            else:
                create_owner()
                return JsonResponse({'message':data}, status=201)
        except:
            return JsonResponse({'message':'Error!!'}, status=400)

    def get(self, request):
        data  = json.loads(request.body)
        owner_profile = Owner.objects.filter(name=data['name'])
        result = []
        try:
            if owner_profile.exists():
                for info in owner_profile:
                    result.append({
                        'name'  : info.name,
                        'email' : info.email,
                        'age'   : info.age
                    })
                return JsonResponse({'result':result}, status=200)
            else:
               return JsonResponse({'message':'Unregistered owner!!'}, status=404) 
        except:
            return JsonResponse({'message':'Error!'}, status=400)
        

class DogProfilerView(View):
    def post(self, request):
        data  = json.loads(request.body)

        def create_dog():
            Dog.objects.create(
                name     = data['dog_name'],
                age      = data['dog_age'],
                owner_id = data['dog_owner_id']
            )

        try:
            if Dog.objects.filter(name=data['dog_name']).exists():
                dog = Dog.objects.get(name=data['dog_name'])

                if data['dog_age'] == dog.age and data['dog_owner_id'] == dog.owner_id:
                    return JsonResponse({'message':'Registered dog!'}, status=409)
                else:
                    create_dog()
                    return JsonResponse({'message':data}, status=201)
            else:
                create_dog()
                return JsonResponse({'message':data}, status=201)
        except:
            return json({'message':'Error!!'}, status=400)
        
    def get(self, request):
        data  = json.loads(request.body)
        dog_profile = Dog.objects.filter(name=data['name'])
        result = []

        try:
            if dog_profile.exists():
                for info in dog_profile:
                    owner = Owner.objects.get(id=info.owner_id)
                    result.append({
                        'name'  : info.name,
                        'age'   : info.age,
                        # 'owner' : Owner.objects.get(id=[info.owner_id])
                        'owner' : owner.name
                    })
                return JsonResponse({'result':result}, status=200)
            else:
               return JsonResponse({'message':'Unregistered dog!!'}, status=404) 
        except:
            return JsonResponse({'message':'Error!'}, status=400)
        