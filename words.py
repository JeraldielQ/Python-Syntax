def print_upper_words(words):
    """Print each word in words that starts with the letter 'e' in uppercase."""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())
