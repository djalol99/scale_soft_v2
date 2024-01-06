from django.views.generic import TemplateView
from devices.models import Scale, IPCamera

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['scales'] = Scale.objects.all()
        kwargs['ipcameras'] = IPCamera.objects.all()
        return super().get_context_data(**kwargs)
    