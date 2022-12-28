
# try [except*hm you need] else finally     raise

try:
    file = open("a_file.txt", 'r')
except FileNotFoundError:
    print("Error file not found!")
    print("Creating file")
    file = open("a_file.txt", 'w')
else:
    data = file.readlines()
    print(data)
finally:
    file.close()
    
