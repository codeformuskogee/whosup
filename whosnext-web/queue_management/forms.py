from django import forms

from .models import QueueMember, Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ()
        widgets = {
            'pin': forms.NumberInput(attrs={'style':'-webkit-text-security: circle; -moz-text-security:circle; text-security:circle;'})
        }

class MemberRemoveForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('pin',)
        widgets = {
            'pin': forms.NumberInput(attrs={'style':'-webkit-text-security: circle; -moz-text-security:circle; text-security:circle;'})
        }
