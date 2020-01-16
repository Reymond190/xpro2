from django.urls import path, include
from .views import timedview,AjaxView


urlpatterns = [
    path('',timedview,name='ongoing' ),
    path('ajax/', AjaxView.as_view(), name='ajax'),
    # path('ajaxx/',ajaxx,name='ajaxx')
]
