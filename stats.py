def count_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    c_count = {} # dictionary to be returned
    for c in text:
        if c.isalpha():
            c = c.lower()
        if c not in c_count:
            c_count[c] = 1
        else:
            c_count[c]+=1
    return c_count
def sort_on(dict):
    return dict["count"]

def sort_char_count(c_count):
    list_of_c_count = []
    for k, v in c_count.items():
        list_of_c_count.append({"c":k, "count":v})
    list_of_c_count.sort(reverse=True,key=sort_on)
    return list_of_c_count
    