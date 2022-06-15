# from django.http import JsonResponse
# import json
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict


from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def api_home(request, *args, **kwargs):

    """
    DRF API view
    """
    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"})
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price'])
        data = ProductSerializer(instance).data
    return Response(data)
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by('?').first()
#     data = {}
#     if instance:
#         # before model_to_dict
#         # data['id'] = instance.id
#         # data['title'] = instance.title
#         # data['content'] = instance.content
#         # data['price'] = instance.price

#         data = model_to_dict(instance, fields=['id', 'title', 'price'])

#         # model instance (model data)
#         # turn it python dictionary
#         # return JSON on client
#     return JsonResponse(data)

