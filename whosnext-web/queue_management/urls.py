from django.urls import path
from . import views

urlpatterns = [
    #members
    #/lists/:slug/queuemember/new
    path('q/<slug:queue_name>/', views.new_queuememeber),
    #/lists/:slug (e.g./lists/administration)
    #/lists/:slug

    #admin
    #/users/:id/edit
    #/users/:id/edit

]