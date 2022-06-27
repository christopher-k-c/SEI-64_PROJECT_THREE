from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    #  Record Model Related Paths 
    path('records/', views.RecordList.as_view(), name='records_index'),
    path('records/<int:pk>/', views.RecordDetail.as_view(), name='records_detail'),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete', views.RecordDelete.as_view(), name='records_delete'),




    # # Add Track List
    path('records/<int:record_id>/add_tracklist/', views.add_tracklist, name='add_tracklist'),



    # Artists Display All
    path('artists/', views.ArtistList.as_view(), name = 'artists_index'),
    # # Artist Display Detail 
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name = 'artists_detail'),
    # # Artist Creation 
    # path('artists/create', views.ArtistCreate.as_view(), name = 'artists_create'),
    # # Artist Update
    path('artists/<int:pk>/update', views.ArtistUpdate.as_view(), name = 'artists_update'),
    # # Artist Delete
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name = 'artists_delete'),


    # Associate a Artist with Records (M:M)
 


]