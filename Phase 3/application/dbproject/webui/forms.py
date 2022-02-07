from django.forms import ModelForm, Textarea
from .models import *

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
            'test': Textarea()
        }


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class BankaccountForm(ModelForm):
    class Meta:
        model = Bankaccount
        fields = '__all__'

class CreatebankaccountrequestForm(ModelForm):
    class Meta:
        model = Createbankaccountrequest
        fields = '__all__'


class CreatecardrequestForm(ModelForm):
    class Meta:
        model = Createcardrequest
        fields = '__all__'


class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeescheduleForm(ModelForm):
    class Meta:
        model = Employeeschedule
        fields = '__all__'


class PaybillForm(ModelForm):
    class Meta:
        model = Paybill
        fields = '__all__'

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'


class QarzolhasanaForm(ModelForm):
    class Meta:
        model = Qarzolhasana
        fields = '__all__'

class RealpersonForm(ModelForm):
    class Meta:
        model = Realperson
        fields = '__all__'


class SavingForm(ModelForm):
    class Meta:
        model = Saving
        fields = '__all__'

class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = '__all__'


class UserrequestForm(ModelForm):
    class Meta:
        model = Userrequest
        fields = '__all__'

class WiretransferForm(ModelForm):
    class Meta:
        model = Wiretransfer
        fields = '__all__'


class WithdrawForm(ModelForm):
    class Meta:
        model = Withdraw
        fields = '__all__'


