"""
Open the provinces.txt file for reading.
Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
Print the entire list.
Remove the first element from the list.
Remove the last element from the list.
Replace all occurrences of "AB" in the list with "Alberta".
Count the number of elements that are "Alberta" and print that number.
"""

def file_to_list(file):
    with open(file, 'rt') as file:
        provinces_list = file.readlines()
    return provinces_list

def ab_to(list):
    for i in range(len(list)):
        if list[i] == "AB\n":
            list[i] = "Alberta"

def count_alberta(list):
    counter = 0
    for i in range(len(list)):
        if list[i] == "Alberta":
            counter += 1
    return counter

def main():
    provinces_list = file_to_list('provinces.txt')
    print(provinces_list)

    provinces_list.pop(0)

    provinces_list.pop()

    ab_to(provinces_list)

    print(provinces_list)

    alberta_freq = count_alberta(provinces_list)
    print(f"Alberta appears {alberta_freq} times")

    

main()