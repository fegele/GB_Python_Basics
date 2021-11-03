with open("text.txt", 'r') as file:
    text = file.readlines()
lines_count = len(text)
print(f'The file contains {lines_count} lines.')
for index, line in enumerate(text):
    words = line.split()
    words_count = len(words)
    print(f"Line #{index + 1}: {words_count} words")
