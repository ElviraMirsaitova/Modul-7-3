class WordsFinder:
    def __init__(self, *files: str):
        self.files = files
        self.list1 = []
        self.list1.extend(files)

    def get_all_words(self):
        all_words = {}
        for file_name in self.list1:
            with open(file_name, 'r', encoding='utf-8') as f:
                slova = []
                for line in f.readlines():
                    line = line.strip().lower()
                    for symbol in (',', '.', '=', '!', '?', ';', ':', ' - '):
                        line = line.replace(symbol,' ')
                    l = []
                    for word in line:
                        if word:
                            l.append(word)
                    slova.extend(line.split(' '))
            all_words[file_name] = slova
        return all_words

    def find(self, word):
        all_wordss = self.get_all_words()
        result = {}
        for i, k in all_wordss.items():
            if word.lower() in k:
                result[i] = k.index(word.lower())
        return result

    def count(self, word):
        all_wordss = self.get_all_words()
        result = {}
        for i, k in all_wordss.items():
            if word.lower() in k:
                result[i] = k.count(word.lower())
        return result



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



