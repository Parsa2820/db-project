from django.forms import *
from .models import *

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Card._meta.get_fields()}


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Transaction._meta.get_fields()}

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Account._meta.get_fields()}


class BankaccountForm(ModelForm):
    class Meta:
        model = Bankaccount
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Bankaccount._meta.get_fields()}

class CreatebankaccountrequestForm(ModelForm):
    class Meta:
        model = Createbankaccountrequest
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Createbankaccountrequest._meta.get_fields()}


class CreatecardrequestForm(ModelForm):
    class Meta:
        model = Createcardrequest
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Createcardrequest._meta.get_fields()}


class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Deposit._meta.get_fields()}


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Employee._meta.get_fields()}

class EmployeescheduleForm(ModelForm):
    class Meta:
        model = Employeeschedule
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Employeeschedule._meta.get_fields()}


class PaybillForm(ModelForm):
    class Meta:
        model = Paybill
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Paybill._meta.get_fields()}

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Purchase._meta.get_fields()}


class QarzolhasanaForm(ModelForm):
    class Meta:
        model = Qarzolhasana
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Qarzolhasana._meta.get_fields()}

class RealpersonForm(ModelForm):
    class Meta:
        model = Realperson
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Realperson._meta.get_fields()}


class SavingForm(ModelForm):
    class Meta:
        model = Saving
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Saving._meta.get_fields()}

class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Support._meta.get_fields()}


class UserrequestForm(ModelForm):
    class Meta:
        model = Userrequest
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Userrequest._meta.get_fields()}

class WiretransferForm(ModelForm):
    class Meta:
        model = Wiretransfer
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Wiretransfer._meta.get_fields()}


class WithdrawForm(ModelForm):
    class Meta:
        model = Withdraw
        fields = '__all__'
        widgets = {f.name: TextInput() for f in Withdraw._meta.get_fields()}


