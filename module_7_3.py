from pprint import pprint

PUNCTUATION_MARKS = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as cur_file:
                file_content = cur_file.read()
                for sub_str in PUNCTUATION_MARKS:
                    file_content = (file_content.lower()).replace(sub_str, ' ')
                all_words[file] = str(file_content).split()

        return all_words

    def find(self, word):
        words_dict = self.get_all_words()
        lower_word = str(word).lower()
        res_dict = {}

        for file_name, words_list in words_dict.items():
            res_dict[file_name] = words_list.index(lower_word) + 1 \
                if lower_word in words_list else None

        return res_dict

    def count(self, word):
        words_dict = self.get_all_words()
        lower_word = str(word).lower()
        res_dict = {}

        for file_name, words_list in words_dict.items():
            res_dict[file_name] = words_list.count(lower_word)

        return res_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))