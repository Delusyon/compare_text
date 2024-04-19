import difflib

def highlight_word_diff(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1 = f1.read()
        text2 = f2.read()

    differ = difflib.Differ()
    diff = differ.compare(text1.split(), text2.split())

    highlighted_diff = ''
    for word_diff in diff:
        if word_diff.startswith('- '):  # Removed word
            highlighted_diff += '[' + word_diff + ']'  # Red color
        elif word_diff.startswith('+ '):  # Added word
            highlighted_diff += '[' + word_diff + ']'  # Green color

        # To print all of the words and all highlighted differences, uncomment these two lines
        # else:
        #     highlighted_diff += word_diff + ' '

    return highlighted_diff

# Example usage
file1 = 'reference.txt'
file2 = 'modified.txt'
highlighted_word_diff = highlight_word_diff(file1, file2)
print(highlighted_word_diff)
