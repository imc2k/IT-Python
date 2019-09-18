from banner import banner

banner("ZIP CODE SORTER", "By Isiah.c")
print("")
print("Welcome to the Newaygo County zip code sorter.")

again = 'Y'
while again == 'Y':
    zip_code = int(input("Please enter a zip code:"))
    print(f"{zip_code}")
    if zip_code == 49309:
        print(f"The zip code {zip_code} is for Bitely")
    elif zip_code == 49312:
        print(f"The zip code {zip_code} is for Brohman")
    elif zip_code == 49337:
        print(f"The zip code {zip_code} is for Newaygo")
    elif zip_code == 49412:
        print(f"The zip code {zip_code} is for Fremont")
    elif zip_code == 49413:
        print(f"The zip code {zip_code} is for Fremont")
    elif zip_code == 49327:
        print(f"The zip code {zip_code} is for Grant")
    elif zip_code == 49349:
        print(f"The zip code {zip_code} is for Whitecloud")
    else:
        print("That zip code is not a Newaygo county area Zip")
    again = input("Would you like to enter another zip code?(Y/N) ")

print("Thank you for using the Newaygo County zip code sorter. Goodbye!")


