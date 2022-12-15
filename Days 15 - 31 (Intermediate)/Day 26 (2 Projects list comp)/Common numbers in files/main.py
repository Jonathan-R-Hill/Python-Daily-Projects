def read(file):
    with open(file) as file:
        file_data = file.readlines()
        data = [int(num.replace("\n", '')) for num in file_data]
        return data

file1_data = read("file1.txt")
file2_data = read("file2.txt")

common = [num for num in file1_data if num in file2_data]
print(common)


