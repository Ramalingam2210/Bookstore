from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bookstore
from .serializers import Bookstore_serializers

# Create your views here.
@api_view(['GET'])
def get_Bookstore(request):
    Bookstores=Bookstore.objects.all()
    serializers=Bookstore_serializers(Bookstores,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def create_Bookstore(request):
    serializers=Bookstore_serializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_Bookstore(request,pk):
    product=Bookstore.objects.get(pk=pk)
    serializer=Bookstore_serializers(product,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Book update','user':serializer.data},status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_Bookstore(request,pk):
    product=Bookstore.objects.get(pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def Bookstorebyid(request,pk):
    product=Bookstore.objects.get(pk=pk)
    serializer=Bookstore_serializers(product)
    return Response(serializer.data)

@api_view(['GET'])
def filter_Bookstore(request):
     Author_name=request.query_params.get('Author_name',None)
     Book_name=request.query_params.get('Book_name',None)

     if Author_name:
         products = Bookstore.objects.filter(Author_name__icontains=Author_name)
     elif Book_name:
         products = Bookstore.objects.filter(Book_name__icontains=Book_name)
     else:
         products = Bookstore.objects.all()

     serializer = Bookstore_serializers(products,many=True)
     return Response({'message': 'Book List','products' : serializer.data})
        