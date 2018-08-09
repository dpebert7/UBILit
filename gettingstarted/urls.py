from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),


#ADDED
from hello.views import ubi_chart

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
    #ADDED
    url(r'^ubi_chart/$', ubi_chart, name="ubi_chart"),
]



#ADDED
#url(r'^simple_chart/$', simple_chart, name="simple_chart"),
