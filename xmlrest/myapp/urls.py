from django.urls import path,include
from myapp import views
urlpatterns = [
    path("student",views.CustomViewSet.as_view()),
    path("callxml",views.CallXml.as_view())
]
