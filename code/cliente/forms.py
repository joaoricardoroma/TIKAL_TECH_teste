from django.forms import ModelForm
from .models import Client
from .models import Email
from .models import Telephone


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        exclude = ("client",)


class TelephoneForm(ModelForm):
    class Meta:
        model = Telephone
        fields = '__all__'
        exclude = ("client",)

