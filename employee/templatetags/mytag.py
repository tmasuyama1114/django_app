from django import template # フィルターやタグを登録するために使う templateモジュール

register = template.Library() # タグやフィルタを登録するための初期化処理

# ページングと他のGETメソッドがぶつかった時のためにこういうtemplate_tagを作成する
# フィルタをかけた後にページネイトを行うと、URLに入っていたクエリ文字列が消えてしまうのでちょっとした手続きが必要
@register.simple_tag # デコレータを使うと便利な機能を定義できる
def url_replace(request, field, value): # タグとして使う関数を定義
    """GETパラメータを一部を置き換える。汎用性が高い"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()