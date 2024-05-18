from django.db import models

# Create your models here.
class MEMBER(models.Model):
    member_id = models.AutoField(primary_key=True)
    mem_email = models.CharField(max_length=255, null=False)
    mem_name = models.CharField(max_length=255, null=False)
    mem_imgUrl = models.TextField()
    mem_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)
    mem_age = models.IntegerField()
    mem_gender = models.CharField(max_length=50)
    mem_job = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'dbset_member'
        managed = False