from django.conf.urls import url

from .views import PizzaDeleteView,PizzaUpdateView, PizzaCreateView,PizzaListView,PizzaDetailView


urlpatterns = [
    url(r'^create',PizzaCreateView.as_view(), name='create'),
    url(r'^$',PizzaListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',PizzaDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$',PizzaUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$',PizzaDeleteView.as_view(), name='delete'),

]