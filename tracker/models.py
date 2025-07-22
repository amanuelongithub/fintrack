from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'category' 


class Transaction(models.Model):
    TRANSACTION_TYPE_WITHDRAWAL = 'W'
    TRANSACTION_TYPE_DEPOSIT = 'D'

    TRANSACTION_TYPE_CHOICES = [
        (TRANSACTION_TYPE_WITHDRAWAL, 'Withdrawal'),
        (TRANSACTION_TYPE_DEPOSIT, 'Deposit')
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2) # 📝
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # 📝
    detail = models.CharField(max_length=256)
    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
    date = models.DateField(auto_now_add=True) # 📝

    class Meta:
        db_table = 'transaction' 
