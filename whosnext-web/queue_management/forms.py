from django import forms

from .models import QueueMember, Member

class QueueMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QueueMemberForm, self).__init__(*args, **kwargs)
        member_fields = forms.fields_for_model(Member, exclude=())
        # self.fields = ('queue')
        self.fields.update(member_fields)

    class Meta:
        model = QueueMember
        fields = ('queue',)
