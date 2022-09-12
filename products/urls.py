from django.urls import URLPattern, path
from .views import(
    product_create_view,
    product_detail_view,
    dynamic_delete_view,
    product_list_view,
    dynamic_lookup_view,
    render_initial_data
)

app_name = "products"  # this will use in URL reverse in models.py
urlpatterns = [
    path('delete/<int:my_id>', dynamic_delete_view, name="delete-product"),
    path('list/', product_list_view, name="list-product"),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('lookup/<int:my_id>', dynamic_lookup_view, name="detail-product"),    
    path('initial/', render_initial_data),
]