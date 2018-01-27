from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    email_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Medicine(models.Model):
    med_id = models.AutoField(primary_key=True)
    med_name = models.CharField(max_length=100)
    med_use = models.CharField(max_length=255)
    med_barcode = models.CharField(max_length=100)


class UserMedicine(models.Model):
    user_med_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    use = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    start_date = models.DateField
    end_date = models.DateField

class Volunteer(models.Model):
    volunteer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Donation(models.Model):
    donation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=20)
    medicine = models.ForeignKey(Medicine,on_delete =models.CASCADE)
    expiry_date = models.DateField()
    quantity = models.IntegerField()

class Medicine_Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    quantity = models.IntegerField()


















