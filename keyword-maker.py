_end = '_end_'

def make_trie(words):
    root = dict()

    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end

    return root


kws = type('', (), {})
kws.py = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
          'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
          'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
          'raise', 'return', 'try', 'while', 'with', 'yield']

print(make_trie(kws.py))
