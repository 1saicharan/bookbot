def count_words(file):
    words = file.split()
    return len(words)

def count_letters(file):
    d = {}
    for i in file:
        i = i.lower()
        if i in "abcdefghijklmnopqrstuvwxyz":
            if i in d:
                d[i]+=1
            else:
                d[i]=1
    return d
with open("books/frankenstein.txt") as f:
    
    file_contents = f.read()
    words = count_words(file_contents)
    letters_dict = count_letters(file_contents)
    print("\n....begining the report of books/frakenstein.txt ....")
    print(f"\n {words} words found in the document")
    for i in sorted(letters_dict.items(),key = lambda x:x[1],reverse = True):
        print(f"\n The {i[0]} character was found {letters_dict[i[0]]} times")

    print("\n----- End report ----")


