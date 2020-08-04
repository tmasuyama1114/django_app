from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic # 汎用ビューを使うためのもの
from django.urls import reverse_lazy # 汎用ビューでデータベースの変更(CRUD) を行うためのもの
from .forms import DayCreateForm # forms.pyで作ったクラスをimport
from .models import Day # Dayモデルをimport


class IndexView(generic.ListView): # generic の ListViewクラスを継承
    model = Day # 一覧表示させたいモデルを呼び出し
    # （ListViewクラスで呼び出されたモデル名はモデル名(小文字)_list という変数で html 側で扱える
    # URLも自動で探してくれる：アプリ名/モデル名_list.html という名前でtemplateを探して、viewで呼び出したモデルを渡してくれる
    # 「diary/day_list.html」 という URL で呼び出される
    # templateを別名で指定するときは「template_name = 'diary/index.html」と書くが、書かなければ上記ルールで自動
    paginate_by = 3 # 3記事を基準にページネーション（generic.ListViewはデフォルト機能でページネイトに対応している）

class AddView(generic.CreateView):
    model = Day # 作成したいmodelを指定
    form_class = DayCreateForm # 作成したいformを指定（シンプルなモデルフォームを使うときは「fields = '__all__' と直接ここに書いても OK）
    success_url = reverse_lazy('diary:index')
    # success_url：データベースの変更に成功した場合にリダイレクトさせるページ（今回は「アプリ名:逆引きURL」の形で指定し、結果的に urls.py で指定した「''」が返される）
    # reverse_lazy：viewに対応した「URLの文字列」を返す。今回であれば「/diary/」を返してくれる

class UpdateView(generic.UpdateView): # 考え方は AddView とほぼ同じ
    model = Day
    form_class = DayCreateForm # 新規登録時にDayCreateFormを通して行った処理を改めて行うのでDayCreateFormをほぼそのまま活用できるのじゃ
    success_url = reverse_lazy('diary:index')


class DeleteView(generic.DeleteView):
    model = Day
    # forms は必要ないので個別のtemplats で確認などを行う
    success_url = reverse_lazy('diary:index')


class DetailView(generic.DetailView):
    model = Day # pkはurlで指定しているのでここではmodelを呼び出すだけで済む


