from django.db import models

# Create your models here.
class userlogin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

class addcustomerdetails(models.Model):
    customer_id = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=500)

class addbuilderdetails(models.Model):
    builder_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=500)
    start_date = models.CharField(max_length=500)
    no_of_project = models.CharField(max_length=500)
    web_site = models.CharField(max_length=500)
    email_id = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=500)

class addprojectdetails(models.Model):
    project_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    details = models.CharField(max_length=500)
    start_date = models.CharField(max_length=100)
    plan_image = models.FileField(upload_to='documents/')
    end_date = models.CharField(max_length=100)

class addbookingdetails(models.Model):
    customer_id = models.CharField(max_length=200)
    project_id = models.CharField(max_length=500)
    site_no = models.CharField(max_length=500)
    booking_date = models.CharField(max_length=500)
    cost = models.CharField(max_length=500)


class addsitedetails(models.Model):
    project_id = models.CharField(max_length=200)
    site_no = models.CharField(max_length=500)
    size = models.CharField(max_length=500)
    site_type = models.CharField(max_length=500)
    estimate_cost = models.CharField(max_length=500)

class newreg(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=500)
    city = models.CharField(max_length=500)



