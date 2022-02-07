# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Card(models.Model):
    cardnumber = models.CharField(primary_key=True, max_length=19)
    primarypassword = models.CharField(max_length=32, blank=True, null=True)
    secondarypassword = models.CharField(max_length=32, blank=True, null=True)
    expirationdate = models.DateField(blank=True, null=True)
    cvv1 = models.CharField(max_length=4, blank=True, null=True)
    cvv2 = models.CharField(max_length=4, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    bankaccount = models.ForeignKey('Bankaccount', models.DO_NOTHING, db_column='bankaccount', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_card'


class Transaction(models.Model):
    transactionid = models.BigIntegerField(primary_key=True)
    source = models.ForeignKey('Bankaccount', models.DO_NOTHING, db_column='source', blank=True, null=True, related_name='transaction_source')
    destination = models.ForeignKey('Bankaccount', models.DO_NOTHING, db_column='destination', blank=True, null=True, related_name='transaction_destination')
    field_date = models.DateField(db_column='_date', blank=True, null=True)  # Field renamed because it started with '_'.
    field_description = models.TextField(db_column='_description', blank=True, null=True)  # Field renamed because it started with '_'.
    amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    trackingid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_transaction'


class Account(models.Model):
    realpersonnationalid = models.ForeignKey('Realperson', models.DO_NOTHING, db_column='realpersonnationalid', blank=True, null=True)
    username = models.CharField(primary_key=True, max_length=30)
    email = models.CharField(max_length=50, blank=True, null=True)
    accountpassword = models.CharField(max_length=32, blank=True, null=True)
    phonenumber = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bankaccount(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField(blank=True, null=True)
    balance = models.TextField(blank=True, null=True)  # This field type is a guess.
    iban = models.CharField(max_length=24, blank=True, null=True)
    opendate = models.DateField(blank=True, null=True)
    creatorusername = models.ForeignKey(Account, models.DO_NOTHING, db_column='creatorusername', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bankaccount'


class Createbankaccountrequest(models.Model):
    requestid = models.OneToOneField('Userrequest', models.DO_NOTHING, db_column='requestid', primary_key=True)
    username = models.ForeignKey(Account, models.DO_NOTHING, db_column='username', blank=True, null=True)
    bankaccounttype = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'createbankaccountrequest'


class Createcardrequest(models.Model):
    requestid = models.OneToOneField('Userrequest', models.DO_NOTHING, db_column='requestid', primary_key=True)
    bankaccountid = models.ForeignKey(Bankaccount, models.DO_NOTHING, db_column='bankaccountid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'createcardrequest'


class Deposit(models.Model):
    transactionid = models.OneToOneField(Transaction, models.DO_NOTHING, db_column='transactionid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'deposit'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    nationalid = models.CharField(primary_key=True, max_length=10)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    fathername = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    mobilenumber = models.CharField(max_length=10, blank=True, null=True)
    landlinenumber = models.CharField(max_length=10, blank=True, null=True)
    field_role = models.TextField(db_column='_role', blank=True, null=True)  # Field renamed because it started with '_'.
    monthlysalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    startdate = models.DateField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    addresextra = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Employeeschedule(models.Model):
    emplyeenationalid = models.OneToOneField(Employee, models.DO_NOTHING, db_column='emplyeenationalid', primary_key=True)
    field_weekday = models.TextField(db_column='_weekday')  # Field renamed because it started with '_'. This field type is a guess.
    starthour = models.TimeField(blank=True, null=True)
    endhour = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeeschedule'
        unique_together = (('emplyeenationalid', 'field_weekday'),)


class Paybill(models.Model):
    transactionid = models.OneToOneField(Transaction, models.DO_NOTHING, db_column='transactionid', primary_key=True)
    billid = models.CharField(max_length=13, blank=True, null=True)
    paymentid = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paybill'


class Purchase(models.Model):
    transactionid = models.OneToOneField(Transaction, models.DO_NOTHING, db_column='transactionid', primary_key=True)
    storename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase'


class Qarzolhasana(models.Model):
    id = models.OneToOneField(Bankaccount, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'qarzolhasana'


class Realperson(models.Model):
    nationalid = models.CharField(primary_key=True, max_length=10)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    fathername = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    mobilenumber = models.CharField(max_length=10, blank=True, null=True)
    landlinenumber = models.CharField(max_length=10, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    addresextra = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realperson'


class Saving(models.Model):
    id = models.OneToOneField(Bankaccount, models.DO_NOTHING, db_column='id', primary_key=True)
    profit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saving'


class Support(models.Model):
    requestid = models.OneToOneField('Userrequest', models.DO_NOTHING, db_column='requestid', primary_key=True)
    username = models.ForeignKey(Account, models.DO_NOTHING, db_column='username', blank=True, null=True)
    employeenationid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeenationid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support'


class Userrequest(models.Model):
    requestid = models.BigIntegerField(primary_key=True)
    field_status = models.TextField(db_column='_status', blank=True, null=True)  # Field renamed because it started with '_'. This field type is a guess.
    field_date = models.DateField(db_column='_date', blank=True, null=True)  # Field renamed because it started with '_'.
    response = models.TextField(blank=True, null=True)
    field_description = models.TextField(db_column='_description', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'userrequest'


class Wiretransfer(models.Model):
    transactionid = models.OneToOneField(Transaction, models.DO_NOTHING, db_column='transactionid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'wiretransfer'


class Withdraw(models.Model):
    transactionid = models.OneToOneField(Transaction, models.DO_NOTHING, db_column='transactionid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'withdraw'
