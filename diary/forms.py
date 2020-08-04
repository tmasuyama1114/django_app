from django import forms
from .models import Day


class DayCreateForm(forms.ModelForm): # DjangoのModelFormでは強力なValidationを使える

    class Meta: # 入れ子になっているけどこういうものだと思いましょう
        model = Day # Dayモデルと接続し、Dayモデルの内容に応じてformを作ってくれる
        fields = '__all__' # これはすべて指定するやり方。('title', 'text') とタプルで個別に指定することもできる
