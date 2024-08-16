from django.forms import Form,ModelForm
from clone.models import SignupModel

class SignupForm(ModelForm):
    class Meta:
        model=SignupModel
        fields="__all__"