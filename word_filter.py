class WordFilter:

    def __init__(self, my_filter):
        self.my_filter = my_filter

    def detect(self, text, censored):
        if self.my_filter:
            text = text.replace(self.my_filter, censored)
            return text


def ng_word_list():
    counter = 1

    while True:
        ng_word = (input("NGワード" + str(counter) + ":"))
        print("NGワードを設定しました｡")
        if ng_word == "end":
            break
        counter += 1

        return ng_word


my_filter = WordFilter((ng_word_list()))

print(my_filter.detect("昨日のアーセナルの試合アツかった！", "ピー"))
print(my_filter.detect("昨日のリバプールの試合アツかった！", "ピー"))
