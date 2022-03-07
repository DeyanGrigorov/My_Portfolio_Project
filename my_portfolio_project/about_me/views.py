from django.views.generic import TemplateView


class AboutMe(TemplateView):
    template_name = 'about_me.html'
