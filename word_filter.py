# my_filter = WordFilter("アーセナル")
#
# # NGワードが含まれている場合
# my_filter.detect("昨日のアーセナルの試合アツかった！") # Trueを返す ※出力されるわけではありません！
#
# # NGワードが含まれていない場合
# my_filter.detect("昨日のリバプールの試合アツかった！") # Falseを返す ※出力されるわけではありません！

class WordFilter:

    def __init__(self, my_filter):
        self.my_filter = my_filter

    def detect(self, word):
        return self.my_filter in word


if __name__ == "__main__":
    my_filter = WordFilter("アーセナル")

    print(my_filter.detect("昨日のアーセナルの試合アツかった！"))
    print(my_filter.detect("昨日のリバプールの試合アツかった！"))
