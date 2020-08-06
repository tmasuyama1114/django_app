from .models import Category

# 右側に常にカテゴリ一覧を表示させるための処理
def common(request):
    """テンプレートに常にデータ"""
    context = {
        'category_list': Category.objects.all(),
    }
    return context