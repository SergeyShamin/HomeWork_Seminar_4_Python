'''В текстовом файле удалить все слова, 
которые содержат хотя бы одну цифру.
Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.'''

text = input("Введите текст : ")

def word_has_digit(word):
    for char in word:
        if char.isdigit():
            return True
    return False

def filter_words(text):
    words = text.split()
    result_words = []
    for word in words:
        if not word_has_digit(word):
            result_words.append(word)
    return result_words

print(filter_words(text))