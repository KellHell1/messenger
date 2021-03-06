from django.urls import path
from . import views
from .views import send_friend_request, my_friends, my_friend_request, accept, decline, remove


urlpatterns = [
    path('send_friend_request/<int:id>/', send_friend_request, name='send_friend_request'),
    path('my_friends/', my_friends, name='friends_and_request'),
    path('my_friend_request/', my_friend_request, name='friends_and_request'),
    path('accept/<int:id>', accept, name='accept'),
    path('decline/<int:id>', decline, name='decline'),
    path('remove/<int:id>', remove, name='remove')
]