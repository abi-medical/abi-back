from base import views as base_views


class BaseCreateView(base_views.BaseCreateView):
    template_name = "custom_create/create.html"

    def __init__(self, *args, **kwargs):
        super(BaseCreateView, self).__init__(*args, **kwargs)

class BaseUpdateView(base_views.BaseUpdateView):
    template_name = "custom_update/update.html"

    def __init__(self, *args, **kwargs):
        super(BaseUpdateView, self).__init__(*args, **kwargs)

class BaseDeleteView(base_views.BaseDeleteView):
    template_name = "custom_delete/delete.html"

    def __init__(self, *args, **kwargs):
        super(BaseDeleteView, self).__init__(*args, **kwargs)