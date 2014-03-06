from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^create_template$', 'tpms_survey.api.create_template', name='home'),
    url(r'^create_question$', 'tpms_survey.api.create_question', name='home'),
    url(r'^template$', 'tpms_survey.views.template', name='template'),
    url(r'^get_template$', 'tpms_survey.views.get_template', name='get_template'),
    url(r'^add_template$', 'tpms_survey.views.add_template', name='add_template'),
    url(r'^update_template$', 'tpms_survey.views.update_template', name='update_template'),
    url(r'^delete_template$', 'tpms_survey.views.delete_template', name='delete_template'),
    # url(r'^tpms/', include('tpms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
