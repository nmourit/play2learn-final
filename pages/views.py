from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'