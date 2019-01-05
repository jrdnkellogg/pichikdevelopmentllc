from django.urls import path
from webapp import views

app_name = 'web_application'

urlpatterns = [
    path('firstlisting/',views.firstlisting,name="firstlisting"),
    path('secondlisting/',views.secondlisting,name="secondlisting"),
    path('thirdlisting/',views.thirdlisting,name="thirdlisting")
]
