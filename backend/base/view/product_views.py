from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Product, Review
from ..serializers import ProductsSerializer


@api_view(['GET'])
def get_products(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''

    products = Product.objects.filter(
        name__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(products, 5)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)

    serializer = ProductsSerializer(products, many=True)
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def get_top_products(request):
    products = Product.objects.filter(rating__gte=4).order_by('-rating')
    serializer = ProductsSerializer(products, many=True)
    return serializer.data


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductsSerializer(product, many=False)
    return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def create_product(request):
#     user = request.user
#     data = request.data
#     try:
#         product = Product.objects.create(
#             user=user,
#             name=data['name'],
#             image=data['image'],
#             brand=data['brand'],
#             category=data['category'],
#             description=data['description'],
#             rating=data['rating'],
#             numReviews=data['numReviews'],
#             price=data['price'],
#             countInStock=data['countInStock']
#         )
#         serializer = ProductsSerializer(product, many=False)
#         return Response(serializer.data)
#     except:
#         message = {'detail': 'Product with this datas already exists'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_product(request):
    user = request.user
    product = Product.objects.create(
        user=user,
        name='Sample name',
        price=0,
        brand='Sample brand',
        countInStock=0,
        category='Sample Category',
        description=''
    )
    serializer = ProductsSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_product(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)
    product.name = data['name']
    product.image = data['image']
    product.brand = data['brand']
    product.category = data['category']
    product.description = data['description']
    product.price = data['price']
    product.countInStock = data['countInStock']
    product.save()
    serializer = ProductsSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product has deleted')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_image(request):
    data = request.data
    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)
    product.image = request.FILES.get('products_photo')
    product.save()
    return Response('Image was uploaded')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product_review(request, pk):
    user = request.user
    data = request.data
    product = Product.objects.get(_id=pk)
    already_exists = product.review_set.filter(user=user).exists()
    if already_exists:
        content = {'details': 'Product already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif data['rating'] == 0:
        content = {'details': 'Please select rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        review = Review.objects.create(
            product=product,
            user=user,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment']
        )
        reviews = product.review_set.all()
        product.numReviews = len(reviews)
        total = 0
        for i in reviews:
            total += i.rating
        product.rating = total / len(reviews)
        product.save()
        return Response({'detail': 'Review added'})
