from datetime import date
import sys
import inflect

def convert(my_birthday):
    try:
        my_birthday = date.fromisoformat(my_birthday)
    except:
        sys.exit("Invalid date")

    today = date.today()
    time_to_now = abs(today - my_birthday).days*24*60
    words = inflect.engine().number_to_words(time_to_now).capitalize().replace(" and","")
    return f"{words} minutes"

def main():
    print(convert(input("DOB: ")))

if __name__ == "__main__":
    main()
