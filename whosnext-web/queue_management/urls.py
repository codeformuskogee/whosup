from django.urls import path
from . import views

urlpatterns = [
    #members
    #/lists/:slug/queuemember/new
    path('q/<slug:slug>/', views.list_queuememebers),
    path('q/<slug:slug>/new', views.new_queuememeber),
    path('q/<slug:slug>/<id:id>/remove', views.new_queuememeber),
    #/lists/:slug (e.g./lists/administration)
    #/lists/:slug

    #admin
    #/users/:id/edit
    #/users/:id/edit

]