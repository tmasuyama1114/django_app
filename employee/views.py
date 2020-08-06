from django.views import generic
from .forms import SearchForm
from .models import Employee

# 社員情報の追加は管理ページで行うので簡易で済む
class IndexView(generic.ListView): # 汎用ビューを使用
    model = Employee # モデルを呼び出し
    paginate_by = 1

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        context = super().get_context_data() # 親クラスの model = Employee を get_context_data メソッドで呼び出す
        # self.request.GET と書けば、一度選択した内容が次のページでも選択済みの状態になる（残る）
        context['form'] = SearchForm(self.request.GET)   # 基の辞書に、自身への request で GET（ただ検索）するための form を追加する
        return context

    def get_queryset(self):
        """テンプレートへ渡す「employee_list」を作成する"""
        form = SearchForm(self.request.GET) # 入力された内容をformから取得する呪文
        # 今回はformは空欄でもOKなのでis_validは常にTrueだが、is_validメソッドを呼び出さないと後でformを呼び出せない
        form.is_valid()  # これを行わないと cleaned_dataができなくなる

        # まず全社員情報をここで取得する
        queryset = super().get_queryset()

        # 部署の選択があれば、部署で絞り込み(filter) 
        # ここでDepartMentモデルのインスタンスが格納される
        department = form.cleaned_data['department'] # cleaned_dataでformのデータにvalidationをかけた値を取得できる
        # 選択していれば〜
        if department:
            queryset = queryset.filter(department=department) # 引数はモデルのフィールド名を指定

        # サークルの選択があれば、サークルで絞り込みを行う処理(filter)
        club = form.cleaned_data['club']
        if club:
            queryset = queryset.filter(club=club)
        
        # 結果を返す
        return queryset