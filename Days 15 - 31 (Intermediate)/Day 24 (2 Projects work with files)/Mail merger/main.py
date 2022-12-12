placeholder = "[name]"

with open('names.txt') as n:
    names = n.readlines()

with open('letter.txt', 'r') as file :
    letter_cont = file.read()
        

for name in names:
    stripped_name = name.strip()
    
    # Replace the target string
    new_letter = letter_cont.replace(placeholder, stripped_name)

    # Write the file out again
    filename = f"{stripped_name}.txt"
    path = f"D:\Projects\Python Course\Days 15 - 31 (Intermediate)\Day 24 (work with files)\Mail merger\letters\{filename}"
    with open(path, 'w') as file:
        file.write(new_letter)