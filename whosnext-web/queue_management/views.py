from django.shortcuts import render
from .forms import MemberForm, MemberRemoveForm
from .models import QueueMember, Member, Queue

# Create your views here.
def list_queuememebers(request, slug):
    queue = Queue.objects.get(slug__iexact=slug)
    members = QueueMember.objects.filter(queue_id=queue.id)
    return render(request, 'queue_management/list_queuemembers.html', {'queue': queue, 'members': members})

def new_queuememeber(request, slug):
    queue = Queue.objects.get(slug__iexact=slug)
    # if not queue:
    #     raise Exception('Invalid queue name')
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            QueueMember.objects.create(queue_id=queue.id, member_id=member.id)
    else:
        form = MemberForm()
    return render(request, 'queue_management/queuemember_new.html', {'form': form})

def remove_queuememeber(request, id):
    # if not queue:
    #     raise Exception('Invalid queue name')
    if request.method == "POST":
        form = MemberRemoveForm(request.POST)
        member = Member.objects.filter(id=id, pin=form.data['pin']).first()
        if member:
            member.delete()
    else:
        form = MemberRemoveForm()
    return render(request, 'queue_management/queuemember_new.html', {'form': form})
