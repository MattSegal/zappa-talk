from django.views.generic import TemplateView

from .models import Counter


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        try:
            self.counter = Counter.objects.get()
        except Counter.DoesNotExist:
            self.counter = Counter.objects.create()

        self.counter.count += 1
        self.counter.save()
        return super().get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = self.counter
        return context
