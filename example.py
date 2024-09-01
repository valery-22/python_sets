def find_unique_string(words):
    seen = set()
    duplicates = set()
    
    # First pass: Identify duplicates
    for word in words:
        if word in seen:
            duplicates.add(word)
        else:
            seen.add(word)
    
    # Second pass: Find the last unique string by iterating from the end
    for word in reversed(words):
        if word not in duplicates:
            return word
    
    return ''

# Test cases
print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
print(find_unique_string([]))  # It should print: ''
