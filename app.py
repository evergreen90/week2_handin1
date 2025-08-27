# 基礎要件
# ユーザー一覧表示
# 新規ユーザ追加
# 終了する

from db_config import Customer


def main():
    print(
        """===== Welcome to CRM Application =====
[S]how: Show all users info
[A]dd: Add new user
[Q]uit: Quit application
======================================"""
    )

    while True:
        choice = input("Your command > ")
        # 文字を大文字で処理
        cmd = choice.upper()
        if cmd == "S":
            show()
        elif cmd == "A":
            add()
        elif cmd == "Q":
            print("BYE!")
            exit()
        else:
            print(f"{choice}: command not found")
        print("")

def show():
    for customer in Customer.select():
        print(f"Name: {customer.name} Age: {customer.age}")

def add():
    name = input("New user name: ")
    age = input("New user age: ")

    name = Customer.create(name=name, age=age)
    print(f"add new user: {name.name}")


if __name__ == "__main__":
     main()