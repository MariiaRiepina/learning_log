from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name ='edit_entry'),
    #Page for show all locations
    path('locations/', views.location_list, name='location_list'),
    #Page for show details locations
    path('locations/<int:location_id>/', views.location_detail, name='location_detail'),
    #Page for creating a new location
    path('create_location/', views.create_location, name='create_location'),
    #Page for assigning users to lactions
    path('assign_locations/', views.assign_locations, name='assign_locations'),
]

