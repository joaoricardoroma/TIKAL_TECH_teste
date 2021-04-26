from django.contrib import admin
from django.db import models
from dotenv import load_dotenv
import datetime

load_dotenv()


class Client(models.Model):
    def __str__(self):
        return f"{self.name}, {self.cpf}, {self.gender}"

    name = models.CharField("Nome", max_length=100, null=False)
    rg = models.CharField(max_length=11, null=False)
    cpf = models.CharField(max_length=11, null=False)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=30, choices=[
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino"),
        ("outros", "outros"),
    ])

    @admin.display(
        boolean=False,
        ordering='birth_date',
        description='age'
    )
    def client_age(self):
        timedelta = datetime.datetime.today().date() - self.birth_date
        return int(timedelta.days / 365)


class Email(models.Model):
    def __str__(self):
        return f'{self.email}'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)


class Telephone(models.Model):
    def __str__(self):
        return f'{self.number}, {self.ddd}, {self.number_type}'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ddd = models.CharField(max_length=3)
    number = models.CharField(max_length=9)
    number_type = models.CharField(max_length=30, choices=[
        ("Celular", "Celular"),
        ("Residêncial", "Residêncial"),
        ("Comercial", "Comercial"),
    ])


