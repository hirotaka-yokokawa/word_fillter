class WordFilter:
    def __init__(self, my_filter):
        self.my_filter = my_filter

    def detect(self, text, censored):
        for i in range(0, len(self.my_filter)):
            if self.my_filter[i] in text:
                text = text.replace(self.my_filter[i], censored)
        return text


def ng_word_list():
    counter = 1
    ng_list = []

    while True:
        ng_word = (input("NGワード" + str(counter) + ":"))
        print("他にNGワードを設定しますか? y or n")
        yes_no = input()
        ng_list.append(ng_word)

        if yes_no == "no":
            break

        counter += 1

    return ng_list


my_filter = WordFilter((ng_word_list()))
print(my_filter.detect("昨日のアーセナルの試合アツかった！", "ピー"))
print(my_filter.detect("昨日のリバプールの試合アツかった！", "ピー"))
