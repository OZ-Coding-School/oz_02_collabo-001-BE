from django.shortcuts import render, redirect

# Create your views here.
from dbset.models import MET_REQUEST, MET_SURVEY
from django.views.decorators.csrf import csrf_protect
# from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'post/index.html')

def meet(request):
    meetlist = MET_REQUEST.objects.all()
    return render(request, 'post/meet.html', {'meetlist':meetlist})

def posting(request, pk):
    meet = MET_REQUEST.objects.get(pk=pk)
    surveys = MET_SURVEY.objects.select_related('meet').filter(meet=meet)
    return render(request, 'post/posting.html', {'meet': meet, 'surveys': surveys})

@csrf_protect
def new_post(request):
    if request.method == 'POST':
        def get_joined_values(prefix, count):
            return ', '.join([request.POST.get(f'{prefix}{i}', '') for i in range(1, count + 1) if request.POST.get(f'{prefix}{i}', '')])

        process = get_joined_values('process', 3)
        out_links = get_joined_values('out_links', 3)
        address = get_joined_values('address', 2)
        re_payment = get_joined_values('re_payment', 4)

        posting = MET_REQUEST.objects.create(
            re_image=request.FILES.get('re_image'),
            re_category=request.POST.get('re_category'),
            re_title=request.POST.get('re_title'),
            re_meetbrief=request.POST.get('re_meetbrief'),
            content=request.POST.get('content'),
            re_supplies=request.POST.get('re_supplies'),
            preparation_materials=request.POST.get('preparation_materials'),
            process=process,
            out_links=out_links,
            regular_activity=request.POST.get('regular_activity'),
            schedule=request.POST.get('schedule'),
            address=address,
            mbr_age=request.POST.get('mbr_age'),
            mbr_num=request.POST.get('mbr_num'),
            mbr_content=request.POST.get('mbr_content'),
            pick_method=request.POST.get('pick_method'),
            re_challenge=request.POST.get('re_challenge'),
            re_payment=re_payment,
        )

        for i in range(1, 16):
            survey = request.POST.get(f'survey{i}', '')
            if survey:  # survey가 존재할 경우에만 저장
                MET_SURVEY.objects.create(su_survey=survey, meet=posting)

        posting.save()        
        return redirect('/planpeak/post/global_search')
    return render(request, 'post/new_post.html')

def remove_post(request, pk):
    post = MET_REQUEST.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/planpeak/post/global_search/')
    return render(request, 'post/remove_post.html', {'Post': post})
