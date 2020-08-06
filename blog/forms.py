from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):

    # *args: 複数の引数をタプルとして受け取る
    # **kwargs: 複数のキーワード引数を辞書として受け取る
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 特殊処理を上書き
        for field in self.fields.values():
            # form内のすべてのフィールドのclass属性(css)にform-controlという属性を上書きの形で追加
            field.widget.attrs['class'] = 'form-control'

    # モデルフォームのお約束
    class Meta:
        model = Comment
        # 飛んでくるときには Post の pk がわかっている
        # 一部のフィールドのみを指定
        fields = ('name', 'text')