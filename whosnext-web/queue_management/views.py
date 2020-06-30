from django.shortcuts import render
from .forms import MemberForm
from .models import QueueMember, Member, Queue

# Create your views here.
def new_queuememeber(request, queue_name):
    queue = Queue.objects.get(name=queue_name)
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
