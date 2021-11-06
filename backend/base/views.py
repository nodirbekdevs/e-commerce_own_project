from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_routes(request):
    routes = [
        ' ===== Products ===== ',

        'GET      /api/products/',
        'PUT      /api/products/upload/',
        'POST      /api/products/<id>/reviews/',
        'GET      /api/products/top/',
        'GET      /api/products/<id>/',
        'DELETE   /api/products/delete/<id>/',
        'PUT      /api/products/update/<id>/',
        'POST     /api/products/create/',

        ' ===== Users ===== ',

        'GET       /api/users/',
        'POST      /api/users/register/',
        'POST      /api/users/login/',
        'POST      /api/users/logout/',
        'GET       /api/users/profile/',
        'PUT       /api/users/profile/update/',
        'GET       /api/users/<id>/',
        'PUT       /api/users/update/<id>/',
        'DELETE    /api/users/delete/<id>/',

        ' ===== Orders =====',

        'GET   /api/orders/',
        'GET   /api/orders/<id>/',
        'GET   /api/orders/myOrders/',
        'POST  /api/orders/add/',
        'PUT   /api/orders/<id>/pay/',
        'PUT   /api/orders/<id>/deliver/',
    ]
    return Response(routes)


