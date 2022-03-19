from django.views.generic import TemplateView


class ContactPage(TemplateView):
    template_name = 'contact.html'
