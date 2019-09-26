from banner import banner
import os
banner("HTML TAG COUNTER", "By Isiah.c")




def get_full_path(name):
    filename = os.path.join(".","testing", "facade_book.html")
    return filename

def load(filename):
    data = []
    print(f"..... loading from {filename}")

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def tag(text):
    count = 0
    prev_char = None
    for char in text:
        if char == "<":
            count += 1
        if char == "/" and prev_char == "<":
            count -= 1
        prev_char = char

    return count


again = 'Y'
while again == 'Y':

    print("Welcome to the HTML tag counter")
    print("")
    filename = input("Please enter the name of an HTML file:")
    loaded_file = load(filename)
    tag_count = 0
    for line in loaded_file:
        tag_count += tag(line)
    print(f"The file has {tag_count} tags.")

    again = input("Would you like to enter another HTML file (Y/N)? ")

print("")
print("Thank you for useing the HTML Tag counter. Goodbye!")














