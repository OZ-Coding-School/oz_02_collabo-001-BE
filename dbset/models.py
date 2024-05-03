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
    
class MET_ROLE(models.Model):
    mem_role_id = models.IntegerField()
    member_id = models.ForeignKey(MEMBER, on_delete=models.CASCADE)
    ro_rloe = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    meeting_name = models.CharField(max_length=100)
    ro_position = models.CharField(max_length=100)
    post_id = models.IntegerField()
    mem_deposit = models.BooleanField()
    mem_category = models.CharField(max_length=255)

class MET_REQUEST(models.Model):
    met_request_id = models.AutoField(primary_key=True)
    insta_url = models.TextField()
    youtub_url = models.TextField()
    et_url = models.TextField()
    re_title = models.CharField(max_length=255, null=False)
    re_content = models.TextField(null=False)
    date_of_meeting = models.DateField(null=False)
    re_supplies = models.CharField(max_length=255)
    re_image = models.ImageField()
    re_meetbrief = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True, null=False)
    business_area = models.CharField(max_length=50)
    regular_activity = models.CharField(max_length=10)
    online_offline = models.CharField(max_length=10)
    re_challenge = models.CharField(max_length=10)
    re_category = models.CharField(max_length=10)
    participation_fee = models.IntegerField()
    preparation_materials = models.TextField()
    end_of_positing = models.IntegerField()
    re_bank = models.CharField(max_length=50)
    deposit_account = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True)


class MET_COMMENT(models.Model):
    met_comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(MET_ROLE, on_delete=models.CASCADE, null=False)
    member_id = models.ForeignKey(MEMBER, on_delete=models.CASCADE, null=False)
    co_content = models.TextField()
    display_name = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True)

class MET_ATTENDANCE(models.Model):
    met_attendance_id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(MEMBER, on_delete=models.CASCADE)
    post_id = models.ForeignKey(MET_ROLE, on_delete=models.CASCADE)
    attendance_check = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True)


class MET_CHALLENGE(models.Model):
    met_challenge_id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(MEMBER, on_delete=models.CASCADE, null=False)
    post_id = models.ForeignKey(MET_ROLE, on_delete=models.CASCADE, null=False)
    ch_send = models.CharField(max_length=100)
    ch_send_check = models.BooleanField()
    ch_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True)

    

class ALM_MESSAGE(models.Model):
    alm_message_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(MET_ROLE, on_delete=models.CASCADE, null=False)
    member_id = models.ForeignKey(MEMBER, on_delete=models.CASCADE, null=False)
    me_eta = models.DateField()
    me_send = models.IntegerField()
    me_message= models.TextField()
    me_category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
class MET_SURVEY(models.Model):
    met_survey_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(MET_ROLE, on_delete=models.CASCADE, null=False)
    member_id = models.ForeignKey(MEMBER, on_delete=models.CASCADE, null=False)
    su_survey = models.TextField()
    su_answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True)
    

class MET_CATEGORY(models.Model):
    met_category_id = models.IntegerField()
    post_id = models.ForeignKey(MET_ROLE, on_delete=models.CASCADE)
    met_keyword_id = models.IntegerField()
    
class MET_KEYWORD(models.Model):
    met_keyword_id = models.IntegerField()
    keyword_list = models.CharField(max_length=50)