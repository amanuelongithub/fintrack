from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def list_transactions(request):
    if request.method == 'GET':
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Transaction Saved!')

@api_view(['GET', 'PUT', 'DELETE'])
def get_transaction(request, id):
    transaction = get_object_or_404(Transaction, pk=id)
    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Transaction Updated!")
    elif request.method == 'DELETE':
        transaction.delete()
        return Response("Transaction Deleted!")

@api_view(['GET'])
def get_summary(request):
    transaction = get_object_or_404(Transaction)
    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
 
 