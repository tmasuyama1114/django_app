from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /diary　※name='index' は view や templates からこの URL を逆引きして呼び出すためのもの
    path('add/', views.AddView.as_view(), name='add'), # /diary/add
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'), # diary/update/1　※特定のレコードに対して処理を行うので <int:pk> として pk で識別
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'), # /diary/delete/1　※特定のレコードに対して処理を行うので pk で識別
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'), # /diary/detail/1　※特定のレコードに対して処理を行うので pk で識別
]
