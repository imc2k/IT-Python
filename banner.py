
def banner(title, author):

    title_length = len(title)

    byline = f"{author}"

    byline_length = len(byline)

    banner_length = max(title_length, byline_length) +8

    print("=" * banner_length)
    print(f"{title:^{banner_length}}")
    print(f"{byline:^{banner_length}}")
    print("=" * banner_length )
    print("")

banner("Custom Banner", "Maker")

name = input("what is your name?")
title = input("what is your quest?")
banner(Quest,name)