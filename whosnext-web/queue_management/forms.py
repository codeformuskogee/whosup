from django import forms

from .models import QueueMember, Member

class QueueMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QueueMemberForm, self).__init__(*args, **kwargs)
        member_fields = forms.fields_for_model(
            Member,
            exclude=(),
            widgets={
                'pin': forms.NumberInput(attrs={'style':'-webkit-text-security: circle; -moz-text-security:circle; text-security:circle;'})
            }
        )
        print(member_fields)
        self.fields.update(member_fields)

    class Meta:
        model = QueueMember
        fields = ('queue',)