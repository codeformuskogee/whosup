from django.shortcuts import render
from .forms import QueueMemberForm

# Create your views here.
def new_queuememeber(request):
    form = QueueMemberForm()
    return render(request, 'queue_management/queuemember_new.html', {'form': form})