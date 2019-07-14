from django.urls import include, path
from blog import (
    views,
    form_view,
)

urlpatterns = [
    # path('', views.list_posts),

    # http://127.0.0.1:8000/blog/
    path('', views.PostList.as_view(), name = 'post-list'),

    # http://127.0.0.1:8000/blog/PK/
    path('<int:pk>/', views.PostDetail.as_view(), name = 'post-detail'),
    # path('<int:pk>/', views.show_detail, name = 'post-detail'),  

    # http://127.0.0.1:8000/blog/new/
    path('new/', views.PostCreate.as_view(), name = 'post-create'),
    
    # http://127.0.0.1:8000/blog/1/edit/
    path('<int:pk>/edit/', views.PostUpdate.as_view(), name='post-update'),

    # http://127.0.0.1:8000/blog/1/delete/
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),



    path('model-form/', views.model_form_view),

    path('basic-form/', form_view.basic_form_view),
]   