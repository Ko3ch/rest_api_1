from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
# Create your views here.

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        # before model_to_dict
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        data = model_to_dict(model_data, fields=['id', 'title', 'price'])

        # model instance (model data)
        # turn it python dictionary
        # return JSON on client
    return JsonResponse(data)

