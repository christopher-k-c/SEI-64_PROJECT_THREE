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
    path('records/<int:pk>/add_tracklist/', views.add_tracklist, name='add_tracklist'),

    # Signup Route/URL
    path('accounts/signup/', views.signup, name='signup'),
]