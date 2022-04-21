class MyStack:
    def __init__(self):
        self.stack: list = []  # データを格納するスタック

    # 文字列をスタックに格納する。input...格納したい文字列
    def push(self, _input: str) -> str:
        # ここに処理を書いて下さい
        self.stack.append(_input)
        # print(self.stack)
        return _input


    # スタックから１つ値を取り出す
    def pop(self) -> str:
        # ここに処理を書いて下さい
        self.stack.pop()
        # print(self.stack)
        return "pop呼ばれた"


    # スタックの要素数をチェックし、要素数を返却
    def checkLength(self) -> int:
        # ここに処理を書いて下さい
        return len(self.stack)