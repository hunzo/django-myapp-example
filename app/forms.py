from .models import EmailGroupList, EmailList, RecipientList
from django import forms


class AddEmailForm(forms.ModelForm):
    class Meta:
        model = EmailList
        fields = "__all__"


class AddEmailToGroupForm(forms.ModelForm):
    class Meta:
        model = EmailGroupList
        fields = "__all__"


class AddEmailGroupToRecipientListForm(forms.ModelForm):
    class Meta:
        model = RecipientList
        fields = "__all__"


class UploadFileForm(forms.Form):
    file = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={"class": "form-control"}
        )
    )
