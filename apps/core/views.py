from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import EntryForm
from .models import News, Session, LightningTalk


def get_username(user):
    social_auth = user.social_auth.last()
    if not social_auth:
        return (None, '')
    provider = social_auth.provider
    if provider == 'github':
        username = social_auth.extra_data.get('login')
    elif provider == 'twitter':
        username = social_auth.extra_data.get('access_token').get('screen_name')
    return provider, username


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['keynote_sessions'] = Session.objects.filter(is_active=True, is_keynote=True)
        context['sessions'] = Session.objects.filter(is_active=True, is_keynote=False)
        context['lt_sessions'] = LightningTalk.objects.filter(is_active=True)
        context['news_list'] = News.objects.filter(is_active=True)
        context['status_accepting'] = settings.PUBLICATION_STATUS == settings.PUBLICATION_STATUS_ACCEPTING
        context['status_end_accepting'] = settings.PUBLICATION_STATUS == settings.PUBLICATION_STATUS_END_ACCEPTING
        context['status_public'] = settings.PUBLICATION_STATUS == settings.PUBLICATION_STATUS_PUBLIC
        context['status_preparing'] = settings.PUBLICATION_STATUS == settings.PUBLICATION_STATUS_PREPARING
        context['connpass_url'] = settings.CONNPASS_URL

        return context


class EntryFormView(FormView):
    template_name = 'form.html'
    form_class = EntryForm
    success_url = reverse_lazy('entry-complete')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        provider, username = get_username(self.request.user)
        context['username'] = username
        context['provider'] = provider
        return context

    def form_valid(self, form):
        form.save()

        provider, username = get_username(self.request.user)
        form.cleaned_data.update({
            'provider': provider,
            'username': username,
        })

        send_mail(
            settings.ACCEPTING_EMAIL_TO_ADMIN_SUBJECT,
            render_to_string('email/entry-admin.txt', form.cleaned_data),
            form.cleaned_data.get('email'),
            settings.ADMIN_EMAILS_TO,
            fail_silently=False,
        )

        send_mail(
            settings.ACCEPTING_EMAIL_TO_USER_SUBJECT,
            render_to_string('email/entry-user.txt', form.cleaned_data),
            settings.ADMIN_EMAIL_FROM,
            [form.cleaned_data.get('email')],
            fail_silently=False,
        )

        return super().form_valid(form)
