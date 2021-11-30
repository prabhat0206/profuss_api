from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

def index(request):
    cat_1 = ProductSerializer(Product.objects.filter(category_id=1), many=True).data
    cat_2 = ProductSerializer(Product.objects.filter(category_id=2), many=True).data
    cat_3 = ProductSerializer(Product.objects.filter(category_id=3), many=True).data
    return JsonResponse([cat_1, cat_2, cat_3], safe=False)


def getDatabyCategory(request, category_id):
    data = ProductSerializer(Product.objects.filter(category_id=category_id), many=True).data
    return JsonResponse(data, safe=False)


def getProductbyID(request, id):
    data = ProductSerializer(Product.objects.get(id=id)).data
    return JsonResponse(data, safe=False)


@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        product_name = request.POST.get('name')
        category = request.POST.get('category')
        category_id = request.POST.get('category_id')
        description = request.POST.get('description')
        offer = request.POST.get('offer')
        price = request.POST.get('price')
        new_product = Product(product_name=product_name, category_id=category_id, description=description, offer=offer, price=price, image=image, category=category)
        new_product.save()
        return JsonResponse({"status": "success"}, safe=False)
