from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("pengguna/", views.user_list, name="user_list"),
    path("mulai/<str:username>/", views.start_conversation, name="start_conversation"),
    path("<int:conversation_id>/", views.conversation_detail, name="conversation"),
    path("<int:conversation_id>/kirim/", views.send_message, name="send_message"),
]
