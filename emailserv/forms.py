from django import forms

from emailserv.models import Emailserv, Message, Client
from users.forms import MixinForm


class EmailservForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Emailserv
        exclude = ('owner', 'created_at', 'status')


class MessageForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('owner', )


class ClientForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('owner', )