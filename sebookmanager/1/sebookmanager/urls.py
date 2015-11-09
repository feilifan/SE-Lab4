from django.conf.urls import patterns, include, url
from sebookmanager import view
# Uncomment the next two lines to enable the admin:
import os.path
ROOT_DIR=os.path.dirname(os.path.dirname(__file__))
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^search_result/$', view.search),
    url(r'^add_book/$', view.add_book),
    url(r'^add_success/$', view.add_success),
    url(r'^book_update/$', view.update),
    url(r'^book_delete/$', view.delete),
    url(r'^book_display/$', view.display),
    url(r'^add_author/$', view.add_author),
    url(r'^$',view.home),
    url(r"^(?P<path>.*)$", \
                "django.views.static.serve", \
                {"document_root": ROOT_DIR,}),
)
