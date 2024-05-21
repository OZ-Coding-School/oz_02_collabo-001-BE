from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import JsonResponse
from dbset.models import MEMBER
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username =request.POST["mem_email"]
        password =request.POST["mem_password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return JsonResponse({"status": "success", "message": "인증성공"})
        else:
            print("인증실패")
            return JsonResponse({"status": "error", "message": "인증실패"}, status=401)

    return JsonResponse({"status": "error", "message": "POST 요청을 사용하세요."}, status=400)

def logout_view(request) :
    logout(request)
    return JsonResponse({"status": "success", "message": "로그아웃 성공"})

def signup_view(request) :

    if request.method == "POST":
        print(request.POST)
        username = request.POST["mem_email"]
        password = request.POST["mem_password"]
        name = request.POST["mem_name"]
        mem_address = request.POST["mem_address"]
        mem_age = request.POST["mem_age"]
        mem_gender = request.POST["mem_gender"]
        mem_consent = request.POST["mem_consent"]
        mem_marketing = request.POST["mem_marketing"]
        
        try:
            user = MEMBER.objects.create_user(username, name, password)
            user.mem_address = mem_address
            user.mem_age = mem_age
            user.mem_gender = mem_gender
            user.mem_consent = mem_consent
            user.mem_marketing = mem_marketing
            user.save()
            return JsonResponse({"status": "success", "message": "회원가입 성공"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "POST 요청을 사용하세요."}, status=400)