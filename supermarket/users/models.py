from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20,
                                validators=[
                                    MinLengthValidator(20, '用户名至少20位')
                                ])
    password = models.CharField(max_length=32)

    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"