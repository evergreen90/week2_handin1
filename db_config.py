import logging
import os
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, IntegerField
from playhouse.db_url import connect
from peewee import SqliteDatabase

# .envの読み込み
load_dotenv(override=True)


# 実行したSQLをログで出力する設定
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# データベースへの接続設定
# db = SqliteDatabase("csm_db.sqlite")  # SQLite固定の場合(この場合はインポートが必要 from peewee import SqliteDatabase)
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get("DATABASE") or "sqlite:///csm_db.sqlite")  # 環境変数が無い場合にデフォルト値として値を設定することも可能

# 顧客のモデル
class Customer(Model):
    """Customer Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()
    age = IntegerField()  # 年齢フィールド

    class Meta:
        database = db
        table_name = "customer"


db.create_tables([Customer])
