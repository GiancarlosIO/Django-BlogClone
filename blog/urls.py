from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    ## post urls
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    # we need to add the /$ to final in the urls
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    # make sure you are using the correct view dude
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    ## comments urls
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),

    ## other urls
    url(r'^about/$', views.AboutView.as_view(), name='about'),
]