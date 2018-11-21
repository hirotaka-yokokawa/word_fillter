class WordFilter:

    def __init__(self, my_filter):
        self.my_filter = my_filter

    def detect(self, text, censored):
        if self.my_filter:
            text = text.replace(self.my_filter, censored)
            return text

if __name__ == "__main__":
    my_filter = WordFilter("アーセナル")

    print(my_filter.detect("昨日のアーセナルの試合アツかった！","ピー"))
    print(my_filter.detect("昨日のリバプールの試合アツかった！","ピー"))
