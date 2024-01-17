from django.contrib import messages
from django.urls import reverse_lazy
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.views import FilterView

from devices import filtersets, models, forms, serializers


class MyCustomDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'devices/confirm_delete.html'
    error_url = None
    success_message = "Muvaffaqiyatli o'chirildi."
    error_message = "O'chirishni amalga oshirib bo'lmadi, chunki katalogdan foydalanilgan"

    def delete(self, request, *args, **kwargs):
        response = None
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, self.success_message)
        except ProtectedError:
            error_message = self.error_message
        except Exception:
            error_message = "O'chirishni amalga oshirib bo'lmadi."

        if response is None:
            messages.error(request, error_message, 'danger')
            if self.error_url is None:
                self.error_url = self.success_url
            response = HttpResponseRedirect(self.error_url)
        return response


class MyCustomCreateView(LoginRequiredMixin, CreateView):
    success_message = "Muvaffaqiyatli yaratildi"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class MyCustomUpdateView(LoginRequiredMixin, UpdateView):
    success_message = "Muvaffaqiyatli yangilandi"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


# Scale
class ScaleListView(LoginRequiredMixin, FilterView):
    template_name = 'devices/scale/scale_list.html'
    model = models.Scale
    filterset_class = filtersets.ScaleFilterSet


class ScaleCreateView(MyCustomCreateView):
    template_name = 'devices/scale/scale_form.html'
    model = models.Scale
    form_class = forms.ScaleForm
    success_url = reverse_lazy('devices:scales')


class ScaleUpdateView(MyCustomUpdateView):
    template_name = 'devices/scale/scale_form.html'
    model = models.Scale
    form_class = forms.ScaleForm
    success_url = reverse_lazy('devices:scales')


class ScaleDeleteView(MyCustomDeleteView):
    model = models.Scale
    success_url = reverse_lazy('devices:scales')


class ScaleDetailAPIView(RetrieveAPIView):
    serializer_class = serializers.ScaleSerializer
    queryset = models.Scale.objects.all()


# IP Camera
class IPCameraListView(LoginRequiredMixin, FilterView):
    template_name = 'devices/camera/camera_list.html'
    model = models.IPCamera
    filterset_class = filtersets.IPCameraFilterSet


class IPCameraCreateView(MyCustomCreateView):
    template_name = 'devices/camera/camera_form.html'
    model = models.IPCamera
    form_class = forms.IPCameraForm
    success_url = reverse_lazy('devices:cameras')


class IPCameraUpdateView(MyCustomUpdateView):
    template_name = 'devices/camera/camera_form.html'
    model = models.IPCamera
    form_class = forms.IPCameraForm
    success_url = reverse_lazy('devices:cameras')


class IPCameraDeleteView(MyCustomDeleteView):
    model = models.IPCamera
    success_url = reverse_lazy('devices:cameras')
