from django.db import models

# Create your models here.

class Account(models.Model):
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  type = models.CharField(max_length=20)
  no_of_signers = models.IntegerField()

  def __str__(self):
    return self.id

class Client(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  email = models.EmailField()

  def __str__(self):
    return self.id

class PhoneNumbers(models.Model):
  phone_number = models.CharField(max_length=20)
  client = models.ForeignKey(Client, on_delete=models.CASCADE)

  def __str__(self):
    return self.id

class Address(models.Model):
  address = models.CharField(max_length=100)
  client = models.ForeignKey(Client, on_delete=models.CASCADE)

  def __str__(self):
    return self.id

class AccountOwner(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  role = models.CharField(max_length=20)

  def __str__(self):
    return self.id

class Statement(models.Model):
  note = models.CharField(max_length=100)
  initiator = models.ForeignKey(Client, on_delete=models.CASCADE)
  from_account = models.ForeignKey(Account, on_delete=models.CASCADE)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)
  is_confirmed = models.BooleanField(default=False)

  def __str__(self):
    return self.id

class Cosigner(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  statement = models.ForeignKey(Statement, on_delete=models.CASCADE)

  def __str__(self):
    return self.id

class Transaction(models.Model):
  to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='to_account')
  from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='from_account')
  amount = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.id

class AccountHistory(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  operation = models.CharField(max_length=20)
  account_owner = models.ForeignKey(AccountOwner, on_delete=models.CASCADE)

  def __str__(self):
    return self.id
