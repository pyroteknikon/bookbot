def get_num_words(text):
    word_list = text.split()
    num_words = 0
    for words in word_list:
        num_words += 1 
    return num_words


def get_num_chars(text):
    lower_case = text.lower()
    num_chars = {}
    for word in lower_case:
        if word in num_chars:
            num_chars[word] += 1
        else:
            num_chars[word] = 1
    return num_chars

def format_report(chars):
    report = []
    for char in chars:
        if char.isalpha():
            number = chars[char]
            small_dict = {"char": char, "num": number}
            report.append(small_dict)
    report.sort(reverse=True, key=sort_on)
    return report

def sort_on(report):
    return report["num"]
