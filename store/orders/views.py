from django.views.generic import CreateView
# from django.views.generic import TemplateView


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
