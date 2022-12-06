from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    clients = Client.objects.all()
    accounts = Account.objects.all()
    statements = Statement.objects.all()
    context = {
        'clients': clients,
        'accounts': accounts,
        'statements': statements
    }
    return render(request, 'index.html', context)

def new_client(request):
  return render(request, 'new_client.html')

def create_client(request):
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone')
    address = request.POST.get('address')
    client = Client(first_name=first_name, last_name=last_name, password=password)
    client.save()
    phone = PhoneNumbers(phone_number=phone_number, client=client)
    phone.save()
    addr = Address(address=address, client=client)
    addr.save()
    return redirect('index')

def new_account(request):
  clients = Client.objects.all()
  context = {
    'clients': clients
  }
  return render(request, 'new_account.html', context)

def create_account(request):
  if request.method == 'POST':
    balance = request.POST.get('balance')
    type = request.POST.get('type')
    no_of_signers = request.POST.get('signers')
    account = Account(balance=balance, type=type, no_of_signers=no_of_signers)
    account.save()
    # get client id's from form
    client_ids = request.POST.getlist('client_ids')
    for client_id in client_ids:
      client = Client.objects.get(id=client_id)
      account_owner = AccountOwner(client=client, account=account)
      account_owner.save()
    return redirect('index')

def new_statement(request):
  clients = Client.objects.all()
  accounts = Account.objects.all()
  context = {
    'clients': clients,
    'accounts': accounts
  }
  return render(request, 'new_statement.html', context)

def create_statement(request):
  if request.method == 'POST':
    note = request.POST.get('note')
    initiator_id = request.POST.get('initiator')
    initiator = Client.objects.get(id=initiator_id)
    from_account_id = request.POST.get('from_account')
    from_account = Account.objects.get(id=from_account_id)
    total_amount = request.POST.get('total_amount')
    statement = Statement(note=note, initiator=initiator, from_account=from_account, total_amount=total_amount)
    statement.save()
    return redirect('index')
