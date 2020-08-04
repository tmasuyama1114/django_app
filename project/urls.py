from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/', include('diary.urls')),  # /diary で日記アプリケーション
    path('blog/', include('blog.urls')),  # /blog で、ブログアプリケーション
    path('employee/', include('employee.urls')),  # /employee で、社員管理あぷりけーしょん
]
