from django.urls import path
# Импортируем созданное нами представление
from .views import Postlist, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', Postlist.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]