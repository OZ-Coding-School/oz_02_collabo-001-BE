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
    re_image = models.ImageField(upload_to='images/', blank=True, null=True)
    re_category = models.CharField(max_length=10)
    re_title = models.CharField(max_length=255)
    re_meetbrief = models.CharField(max_length=255)
    re_content = models.TextField(null=True)
    re_supplies = models.CharField(max_length=255, null=True)
    preparation_materials = models.TextField(null=True)
    proc_title = models.CharField(max_length=255, null=True)
    proc_time = models.CharField(max_length=255, null=True)
    proc_content = models.CharField(max_length=255, null=True)
    insta_url = models.TextField(null=True)
    youtub_url = models.TextField(null=True)
    et_url = models.TextField(null=True)
    regular_activity = models.CharField(max_length=10, null=True)
    date_of_meeting = models.TextField(null=True)
    online_offline = models.CharField(max_length=10, null=True)
    business_area = models.CharField(max_length=50, null=True)
    mbr_age = models.CharField(max_length=10, null=True)
    mbr_num = models.CharField(max_length=10, null=True)
    mbr_content = models.TextField(null=True)
    sel_method = models.CharField(max_length=50, null=True)
    # 선발 (설문 최대 15개, null=True)
    re_challenge = models.CharField(max_length=10, null=True)
    participation_check = models.CharField(max_length=10, null=True)
    participation_fee = models.CharField(max_length=50, null=True)
    re_bank = models.CharField(max_length=50, null=True)
    deposit_account = models.CharField(max_length=100, null=True)
    refund_content = models.TextField(null=True)
    end_of_positing = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.re_title

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