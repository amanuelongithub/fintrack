from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def get_transaction(request):
    if request.method == 'GET':
        transaction = Transaction.objects.all()
        seri = TransactionSerializer(transaction, many=True)
        return Response(seri.data)
