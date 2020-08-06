from django import forms
from .models import Club, Department


class SearchForm(forms.Form):
    # 各入力欄を属性として定義する
    # ModelChoiceField とすると既存のClubモデルオブジェクトを取ってきて、選択肢で選ばせる
    # requiredは入力の必須性を指定するもの
    club = forms.ModelChoiceField(
        queryset=Club.objects, label='サークル', required=False) # labelはHTMLで表示させるときの説明みたいなもの

    department = forms.ModelChoiceField(
        queryset=Department.objects, label='部署', required=False)