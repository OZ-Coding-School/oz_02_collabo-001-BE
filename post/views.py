from django.shortcuts import render, redirect

# Create your views here.
from dbset.models import MET_REQUEST, MET_SURVEY

# Create your views here.
def index(request):
    return render(request, 'post/index.html')

def meet(request):
    meetlist = MET_REQUEST.objects.all()
    return render(request, 'post/meet.html', {'meetlist':meetlist})

def posting(request, pk):
    meet = MET_REQUEST.objects.get(pk=pk)
    return render(request, 'post/posting.html', {'meet':meet})

def new_post(request):
    if request.method == 'POST':
        if request.FILES['re_image']:
            posting=MET_REQUEST.objects.create(
                # met_request_id=request.POST['met_request_id'],
                re_image=request.FILES['re_image'],
                re_category=request.POST['re_category'],
                re_title=request.POST['re_title'],
                re_meetbrief=request.POST['re_meetbrief'],
                re_content=request.POST['re_content'],
                re_supplies=request.POST['re_supplies'],
                preparation_materials=request.POST['preparation_materials'],
                proc_title = request.POST['proc_title'],
                proc_time = request.POST['proc_time'],
                proc_content = request.POST['proc_content'],
                #=request.POST['#'], 
                insta_url=request.POST['insta_url'],
                youtub_url=request.POST['youtub_url'],
                et_url=request.POST['et_url'],
                regular_activity=request.POST['regular_activity'],
                date_of_meeting=request.POST['date_of_meeting'],
                online_offline=request.POST['online_offline'],
                business_area=request.POST['business_area'],
                mbr_age=request.POST['mbr_age'],
                mbr_num=request.POST['mbr_num'],
                mbr_content=request.POST['mbr_content'],
                sel_method=request.POST['sel_method'],
                re_challenge=request.POST['re_challenge'],
                participation_check=request.POST['participation_check'],
                participation_fee=request.POST['participation_fee'],
                re_bank=request.POST['re_bank'],
                deposit_account=request.POST['deposit_account'],
                refund_content=request.POST['refund_content'],
                # end_of_positing=request.POST['end_of_positing'],
                # created_at=request.POST['created_at'],
                # modified_at=request.POST['modified_at'],
            )

        else:
            posting=MET_REQUEST.objects.create(
                # met_request_id=request.POST['met_request_id'],
                re_image=request.FILES['re_image'],
                re_category=request.POST['re_category'],
                re_title=request.POST['re_title'],
                re_meetbrief=request.POST['re_meetbrief'],
                re_content=request.POST['re_content'],
                re_supplies=request.POST['re_supplies'],
                preparation_materials=request.POST['preparation_materials'],
                proc_title = request.POST['proc_title'],
                proc_time = request.POST['proc_time'],
                proc_content = request.POST['proc_content'],
                insta_url=request.POST['insta_url'],
                youtub_url=request.POST['youtub_url'],
                et_url=request.POST['et_url'],
                regular_activity=request.POST['regular_activity'],
                date_of_meeting=request.POST['date_of_meeting'],
                online_offline=request.POST['online_offline'],
                business_area=request.POST['business_area'],
                mbr_age=request.POST['mbr_age'],
                mbr_num=request.POST['mbr_num'],
                mbr_content=request.POST['mbr_content'],
                sel_method=request.POST['sel_method'],
                re_challenge=request.POST['re_challenge'],
                participation_check=request.POST['participation_check'],
                participation_fee=request.POST['participation_fee'],
                re_bank=request.POST['re_bank'],
                deposit_account=request.POST['deposit_account'],
                refund_content=request.POST['refund_content'],
                # end_of_positing=request.POST['end_of_positing'],
                # created_at=request.POST['created_at'],
                # modified_at=request.POST['modified_at'],
            )
        posting.save()
        return redirect('/planpeak/post/global_search')
    return render(request, 'post/new_post.html')

def remove_post(request, pk):
    post = MET_REQUEST.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/planpeak/post/global_search/')
    return render(request, 'post/remove_post.html', {'Post': post})
