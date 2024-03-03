from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bill import views
urlpatterns=[
    path('',views.IndexView),
    #Latest try to fetch all data
    path('data/',views.get_data),
]
urlpatterns=format_suffix_patterns(urlpatterns)