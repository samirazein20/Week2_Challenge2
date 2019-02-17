# vowels = "a,e,i,o,u"
# def countVowel(string):
#     count = {}.fromkeys(vowels, 0)

#     for character in string:
#         if character in string:
#             count[character]+=1
#     return count

# string = "dahdah"
# print(countVowel(string))


string_dict = "a,e,i,o,u"
split_string = string_dict.split();

def word_count(a_string):
    string_dict = {}
    for word in a_string.split():
        if word in string_dict:
            string_dict[word] += 1
        else:
            string_dict[word] = 1
    return string_dict

print(word_count('dahdah'));
