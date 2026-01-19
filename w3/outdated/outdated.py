def main():
    list =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    print(get("Date: ",list))

def get(prompt,list):
    while True:
        try:
            #get date
            date = (input(prompt)).strip()
                #9/8/1636 type
            if "/" in date:
                month,date,year = date.split("/")
                month,date,year = int(month),int(date),int(year)    #must int it
                #check valid, <31 days
                if 1 <= month <=12 and 1 <= date <= 31:
                    return (f"{year}-{month:02}-{date:02}")    #02: prefixed with 0, 2digit total

                #September 8, 1636 tyoe
            elif "," in date:
                # Remove comma and split
                date = date.replace(",", "")
                month,date,year = date.split(" ")
                if month in list:
                    # month is accidentally index+1 in list. no need to use dic
                    month = list.index(month) + 1
                    month,date,year = int(month),int(date),int(year)
                    if 1 <= date <= 31:
                        return (f"{year}-{month:02}-{date:02}")

            #not valid -> prompt again
        except (ValueError, KeyError, ZeroDivisionError):
            pass
main()
