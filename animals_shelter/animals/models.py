from django.contrib.auth.models import User
from django.db import models


class Animal(models.Model):
    """
    Animal Model for DataBase Table
    """
    name = models.CharField(max_length=150, verbose_name='кличка')
    age = models.PositiveIntegerField(verbose_name='возраст')
    arrival_date = models.DateTimeField(auto_now_add=True, verbose_name='дата прибытия в приют')
    weight = models.PositiveIntegerField(verbose_name='вес')
    height = models.PositiveIntegerField(verbose_name='рост')
    additional_information = models.TextField(max_length=1000,
                                              null=True, blank=True, verbose_name='дополнительная информация')
    is_deleted = models.BooleanField(default=False, verbose_name='запись удалена')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='приют')

    class Meta:
        verbose_name = 'животное'
        verbose_name_plural = 'животные'
        ordering = ['arrival_date']

    def __str__(self):
        return f"{self.pk}. {self.name}"
