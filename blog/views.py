from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .forms import CommentCreateForm # コメントフォームを呼び出す
from .models import Post, Category, Comment


class IndexView(generic.ListView): # モデルを作ってからListViewとして働きだす
    model = Post
    paginate_by = 10

    # 検索バーにキーワードを入力して検索するための処理
    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at') # created_at を基準にソート（ "-" をつけると降順で並び替え）
        # 呼び出す時に与えられた値をそのままkeywordとして使う
        keyword = self.request.GET.get('keyword')
        if keyword:
            # タイトルで完全一致させるなら queryset = queryset.filter(title=keyword) でよい
            queryset = queryset.filter(
                # 部分一致させるには __icontains と指定し、さらに or 検索をさせるならば Q(xx_cicontains=keyword) | ... とする
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset


# 常に右側に表示させるので常に渡す（context_processorsという手段を使う）
class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10

    # 
    def get_queryset(self):
        """
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        """
        category_pk = self.kwargs['pk'] # Category の pk を取得。 url.py で定義した変数を self.kwargs['pk'] で使える
        queryset = Post.objects.order_by('-created_at').filter(category__pk=category_pk) # CategoryそのものではなくCategoryのpkで絞り込み
        return queryset


class DetailView(generic.DetailView):
    model = Post


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm # モデルフォームを今回は使う

    # formの入力内容のチェックに通ったら呼び出される
    def form_valid(self, form):
        post_pk = self.kwargs['post_pk'] # urlに含まれるpkを渡す
        comment = form.save(commit=False)  # この段階ではまだコメントはDBに保存されていないがコメントモデルのインスタンスは作成されているので書き換えられる
        comment.post = get_object_or_404(Post, pk=post_pk) # 保存する前にモデルインスタンスを作成されているので、post属性をURLのpost_pkで指定する
        comment.save()  # ここでDBに保存
        return redirect('blog:detail', pk=post_pk) # urlのpost_pkを使う
