from django.urls import path
from . import views

urlpatterns = [
    #members
    #/lists/:slug/queuemember/new
    path('', views.new_queuememeber, name='new_queuememeber'),
    #/lists/:slug (e.g./lists/administration)
    #/lists/:slug

    #admin
    #/users/:id/edit
    #/users/:id/edit

]