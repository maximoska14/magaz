from django.urls import path
from myapp.views import index, zap, indexItem

app_name = "site"

urlpatterns = [
    #http://127.0.0.1:8000/site/
    path('', index),
    path('<int:my_id>/', indexItem, name="gl"),
    #http://127.0.0.1:8000/site/Priv/

]