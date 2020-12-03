from django.urls import path

from . import views
from .views import SearchView

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='all-profiles-view'),

    path('myprofile/', views.my_profile_view, name='my-profile-view'),

    path('my-invites/', views.invites_received_view, name='my-invites-view'),
    path('to-invite/', views.invite_profiles_list_view, name='invite-profiles-view'),
    path('send-invite/', views.send_invatation, name='send-invite'),
    path('remove-friend/', views.remove_from_friends, name='remove-friend'),
    path('<slug>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/acctept/', views.accept_invatation, name='accept-invite'),
    path('my-invites/reject/', views.reject_invatation, name='reject-invite'),
    #
    path('search/', SearchView.as_view(), name='search'),
]
