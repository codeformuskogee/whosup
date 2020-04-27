from django import forms

from .models import QueueMember

class QueueMemberForm(forms.ModelForm):

    class Meta:
        model = QueueMember
        fields = ('queue', 'member',)