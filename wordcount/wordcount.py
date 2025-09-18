# Skriv et program der kan tælle antallet af ord i Tobias's tysk stil

essay = "Hallo, ich heisse Tobias. Ich bin 11 Jahre alt. Ich komme aus Dänemark."
 
essay_as_file = open("essay.txt", "r")
content = essay_as_file.read()
print(content)

word_array = essay.split()

# word count
print(len(("Coding Pirates").split()))
# char count
print(len("Coding Pirates"))

