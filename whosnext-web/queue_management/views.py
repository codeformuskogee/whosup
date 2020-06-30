from django.shortcuts import render
from .forms import QueueMemberForm
from .models import QueueMember, Member

# Create your views here.
def new_queuememeber(request):
    if request.method == "POST":
        form = QueueMemberForm(request.POST)
        if form.is_valid():
            queuemember = form.save(commit=False)
            member = Member(full_name=request.POST.get('full_name'), pin=request.POST.get('pin'))
            member.save()
            queuemember.member_id = member.id
            queuemember.save()
    else:
       form = QueueMemberForm()
    return render(request, 'queue_management/queuemember_new.html', {'form': form})