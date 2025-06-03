from greetings import (hello_english, hello_spanish, hello_french, hello_german,
                       goodbye_english, goodbye_spanish, goodbye_french)
from config import DEFAULT_LANGUAGE, SHOW_MENU

name = input("What's your name? ")

if SHOW_MENU:
    print("Choose a language:")
    print("1. English")
    print("2. Spanish")
    print("3. French")
    print("4. German")

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "1":
        print(hello_english(name))
        print(goodbye_english())
    elif choice == "2":
        print(hello_spanish(name))
        print(goodbye_spanish())
    elif choice == "3":
        print(hello_french(name))
        print(goodbye_french())
    elif choice == "4":
        print(hello_german(name))
        print("Auf Wiedersehen!")
    else:
        print("Invalid choice! Using default...")
        print(hello_english(name))
        print(goodbye_english())
else:
    print(hello_english(name))
    print(goodbye_english())