from django.view.generic import TemplateView
import home.views

# Create your views here.


class Index(TemplateView):
    template_name = 'home/index.html'