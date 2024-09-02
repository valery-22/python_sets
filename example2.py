def find_anagram_words(list_1, list_2):
    def sorted_word(word):
        return''.join(sorted(word))
    
    set_2 = {sorted_word(word) for word in list_2} 
    
    return[word for word in list_1 if sorted_word(word) in set_2]# implement this
    

print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []