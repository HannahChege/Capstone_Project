from django.conf.urls import url
from . import views
from djgeojson.views import GeoJSONLayerView
from django.conf import settings
from django.conf.urls.static import static
from . models import food,Restaurant
urlpatterns=[
    url('^$',views.foody,name = 'foody'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^data/$',GeoJSONLayerView.as_view(model=Restaurant),name ='data'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)