from django.views import generic
from .models import Client, Telephone, Email
from .forms import ClientForm, EmailForm, TelephoneForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db import connection


def cliente_query(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
                           SELECT c.*, ce.email 
                           FROM cliente_client c
                           inner join cliente_email ce ON ce.client_id = c.id
                           WHERE email = %s""", [email])
        data = cursor.fetchall()
        return JsonResponse(data, safe=False)


def index(request):
    clientes = Client.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente/index.html', context)


def home(request):
    return render(request, 'cliente/home.html')


def cliente(request, pk=None):
    cliente = None
    if pk is not None:
        cliente = get_object_or_404(Client, pk=pk)
        form_client = ClientForm(instance=cliente)
    else:
        form_client = ClientForm()

    form_email = EmailForm()
    form_telephone = TelephoneForm()

    if request.method == 'POST':
        if request.POST['form'] == "cliente":

            if cliente:
                form_client = ClientForm(request.POST, instance=cliente)
            else:
                form_client = ClientForm(request.POST)

            if form_client.is_valid():
                cliente = form_client.save()
                return redirect('cliente:cliente', pk=cliente.id)

        if request.POST['form'] == "email":
            form_email = EmailForm(request.POST)
            form_email.instance.client = cliente
            if form_email.is_valid():
                form_email.save()

        if request.POST['form'] == "telephone":
            form_telephone = TelephoneForm(request.POST)
            form_telephone.instance.client = cliente
            if form_telephone.is_valid():
                form_telephone.save()

    context = {
        'cliente': cliente,
        'form_client': form_client,
        'form_email': form_email,
        'form_telephone': form_telephone,
    }

    return render(request, 'cliente/cliente.html', context)


def deletar_email(request, pk):
    email = get_object_or_404(Email, pk=pk)
    email.delete()
    return redirect('cliente:cliente', pk=email.client.id)


def deletar_telephone(request, pk):
    telephone = get_object_or_404(Telephone, pk=pk)
    telephone.delete()
    return redirect('cliente:cliente', pk=telephone.client.id)


def deletar_cliente(request, pk):
    cliente = get_object_or_404(Client, pk=pk)
    cliente.delete()
    return redirect('cliente:index')

