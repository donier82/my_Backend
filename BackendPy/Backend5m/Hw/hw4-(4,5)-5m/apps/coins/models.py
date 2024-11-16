from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE, verbose_name='отправитель')
    receiver = models.ForeignKey(User, related_name='received_transactions', on_delete=models.CASCADE, verbose_name='получатель')
    amount = models.IntegerField(verbose_name='количество')
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.CharField(max_length=100, null=True, blank=True, verbose_name='пользовател')
    coins_balance = models.PositiveIntegerField(verbose_name='на балансе', default=4)
