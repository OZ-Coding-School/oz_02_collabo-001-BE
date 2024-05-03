from django.contrib import admin
from .models import (
    MEMBER, MET_ROLE, MET_REQUEST, MET_COMMENT, MET_ATTENDANCE, 
    MET_CHALLENGE, ALM_MESSAGE, MET_SURVEY, MET_CATEGORY, MET_KEYWORD
    )

# Register your models here.
@admin.register(
    MEMBER, MET_ROLE, MET_REQUEST, MET_COMMENT, MET_ATTENDANCE, 
    MET_CHALLENGE, ALM_MESSAGE, MET_SURVEY, MET_CATEGORY, MET_KEYWORD
    )

class MEMBERAdmin(admin.ModelAdmin):
    pass

class MET_ROLEAdmin(admin.ModelAdmin):
    pass

class MET_REQUESTAdmin(admin.ModelAdmin):
    pass

class MET_COMMENTAdmin(admin.ModelAdmin):
    pass

class MET_ATTENDANCEAdmin(admin.ModelAdmin):
    pass

class MET_CHALLENGEAdmin(admin.ModelAdmin):
    pass

class ALM_MESSAGEAdmin(admin.ModelAdmin):
    pass

class MET_SURVEYAdmin(admin.ModelAdmin):
    pass

class MET_CATEGORYAdmin(admin.ModelAdmin):
    pass

class MET_KEYWORDAdmin(admin.ModelAdmin):
    pass