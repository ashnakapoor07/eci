from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name='voting'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^(?P<candidate_id>[0-9]+)/$',views.detail,name='detail'),
    #voting/candidate/add/
    url(r'candidate/add/$',views.AddCandidate.as_view(),name='candidate-add'),

    url(r'^(?P<candidate_id>[0-9]+)/thankyou/$', views.thankyou, name="thankyou"),

    # voting/candidate/2/
    url(r'candidate/(?P<pk>[0-9]+)/$', views.CandidateUpdate.as_view(), name='candidate-update'),

    # voting/candidate/2/delete/
    url(r'candidate/(?P<pk>[0-9]+)/delete/$', views.delete, name='candidate-delete'),


]