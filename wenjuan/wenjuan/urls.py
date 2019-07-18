from django.conf.urls import include, url
from django.contrib import admin
from . import view
urlpatterns = [
    # Examples:
    # url(r'^$', 'wenjuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admins/', view.admin),
    url(r'^$',  view.index_wenjuan),
    url(r'^index/', view.index_wenjuan),
    url(r'^api/', view.api),
    url(r'^res/', view.res),
    url(r'^q_inves/', view.q_inves),
    url(r'^desc/', view.desc),
    url(r'^test/', view.test),
  

]

