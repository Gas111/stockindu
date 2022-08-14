from django.urls import path
from stock.views import lista
urlpatterns = [
    path(r'', lista),
]
