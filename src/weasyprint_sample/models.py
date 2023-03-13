from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

from django.core.validators import RegexValidator


alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


# Create your models here.

class CustomUser(AbstractUser):
    pass

class OrderInfo(models.Model):
    id = models.CharField(primary_key=True, unique=True , null=False, blank=False,
                          max_length=256, editable=False, validators=[alphanumeric])
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default="", null=False)
    np_id = models.CharField(max_length=256)

    order_received_at = models.DateField(auto_now_add=True)
    print_ordered_at = models.DateField()
    will_be_shipping_at = models.DateField()
    updated_at = models.DateField(auto_now=True)

