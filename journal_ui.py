import journal
from banner import banner
banner("Journal","By Isiah.C")

def main():
    run_event_loop()

def run_event_loop():
    filename = "default"
    journal_data = journal.load (filename)#[]

    while True:
        command=input("[L]ist entries, [A]dd an entry, e[X]it: ")

        if command.upper() == "L":
            list_entries(journal_data)
        elif command.upper() == "A":
            add_entry(journal_data)
        elif command.upper() == "X":
            print("x")
            break
        else:
             print("Sorry, I dont understand")
    journal.save(filename ,journal_data)

def list_entries(data):
     print("Your journal entries:")
     entries = reversed(data)
     for  num, entry in enumerate(entries):
         print(f"{num+1} - {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTER> to exit: \n")
    journal.add_entry(entry, data)
    #data.append(entry)

main()