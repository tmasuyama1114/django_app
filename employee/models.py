from django.db import models
from django.utils import timezone

# 部署を表すモデル
class Department(models.Model):
    name = models.CharField('部署名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    # モデルが呼び出されたら部署名を返す
    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField('部活名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name # name なので name= で指定した通り部活名が返される


# 社員を表すモデル
class Employee(models.Model):
    first_name = models.CharField('名', max_length=20)
    last_name = models.CharField('姓', max_length=20)
    email = models.EmailField('メールアドレス', blank=True) # EmailField にすれば自動で Email のバリデーションを行ってくれる
    # Depaartment モデルと紐付け (relation)
    # verbose_name はこのモデルの説明（verbose_name を使って他の関数とかから指定することになる）
    # on_delete=models.PROTECT としておくと、部署のカテゴリが何か消えても紐づく社員情報は消えない
    # ForeignKeyで呼び出すとモデルのインスタンスが丸ごと格納されているのだ
    department = models.ForeignKey(
        Department, verbose_name='部署', on_delete=models.PROTECT,
    )
    # 関連させるモデルのオブジェクトが複数の場合、ManyToManyField を使う (対照的なものとして OneToOneFiledというのもある)
    club = models.ManyToManyField(
        Club, verbose_name='部活',
    )
    # ちなみに後からカラムを追加するときは、default="xx" と指定するか blank=True と入れてから makemigrations する
    created_at = models.DateTimeField('日付', default=timezone.now)

    # selfなのでEmployeeモデルインスタンスオブジェクトが渡される
    # 性、名、部署の3つを渡して return してくれる
    # self.department では Department モデルインスタンスがそのまま渡されて、Department 内で self.name とあるので name が渡される
    def __str__(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.department)
    
    
