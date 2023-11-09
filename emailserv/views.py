from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from emailserv.forms import EmailservForm, MessageForm, ClientForm

from config import settings
from emailserv.models import Emailserv, Message, Client, Mail


class EmailservListView(ListView):
    model = Emailserv


class EmailservDetailView(LoginRequiredMixin, DetailView):
    model = Emailserv

    def get_object(self, **kwargs):
        obj = super().get_object()
        print('object:')
        print(obj.__dict__)
        print(kwargs)
        return obj

    def get_context_data(self, **kwargs):
        cd = super().get_context_data()
        print('context:')
        print(cd)
        print(kwargs)
        return cd


class EmailservCreateView(LoginRequiredMixin, CreateView):
    model = Emailserv
    form_class = EmailservForm
    success_url = reverse_lazy('mailing_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('context in EmailservCreateView(get_context_data):')
        print(context)
        return context

    def form_valid(self, form):
        obj: Emailserv = form.save()
        obj.owner = self.request.user
        obj.save()
        for obj_mail in obj.emails.all():
            status = send_mail(
                subject=obj.message.title,
                message=obj.message.body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[obj_mail.email],
            )
            print(obj_mail.email, status)
        return super().form_valid(form)


class EmailservUpdateView(LoginRequiredMixin, UpdateView):
    model = Emailserv
    form_class = EmailservForm
    success_url = reverse_lazy('mailing_list')

    def form_valid(self, form):
        obj: Emailserv = form.save()
        for obj_mail in obj.emails.all():
            status = send_mail(
                subject=obj.message.title,
                message=obj.message.body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[obj_mail.email],
            )
            print(obj_mail.email, status)
        return super().form_valid(form)


class EmailservDeleteView(LoginRequiredMixin, DeleteView):
    model = Emailserv
    success_url = reverse_lazy('mailing_list')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('name', 'email', 'comment')
    form_class = ClientForm
    success_url = reverse_lazy('clients_list')

    def form_valid(self, form):
        obj: Client = form.save()
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients_list')


class SendMessageCreateView(CreateView):
    template_name = 'email_distribution/message_send.html'
    model = Mail
    fields = ('user', 'message')
    success_url = reverse_lazy('clients_list')

    def form_valid(self, form):
        obj: Mail = form.save()
        status = send_mail(
            subject=obj.message.title,
            message=obj.message.body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[obj.user.email],
        )
        print(status)
        return super().form_valid(form)
