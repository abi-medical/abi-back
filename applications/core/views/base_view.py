from base import views as base_views

class BaseCreateView (base_views.BaseCreateView):
    template_name = "custom_create/create.html"