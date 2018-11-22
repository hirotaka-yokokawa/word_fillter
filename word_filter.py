class WordFilter:

    def __init__(self, my_filter):
        self.my_filter = my_filter

    def detect(self, text, censored):
        if self.my_filter:
            text = text.replace(self.my_filter, censored)
            return text


def ng_word():
    counter = 1

    while True:
        NG_word = input("NGワード" + str(counter) + ":")
        print("NGワードを設定しました｡")
        counter += 1

        if NG_word == "end":
            break

        return NG_word


my_filter = WordFilter((ng_word()))

print(my_filter.detect("昨日のアーセナルの試合アツかった！", "ピー"))
print(my_filter.detect("昨日のリバプールの試合アツかった！", "ピー"))
