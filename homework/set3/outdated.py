numbers = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


while True:
    date = input("Date: ")
    if "," in date:
        date_list = date.replace(",", "").split()
        if len(date_list) != 3:
            continue
        month = date_list[0]
        day = date_list[1]
        year = date_list[2]
        if month in numbers:
            month = numbers[month]
        if month < 10:
            month = "0" + str(month)
        if len(day) == 1:
            day = "0" + day
        print(f"{year}-{month}-{day}")
        break
    elif "/" in date:
        date_list = date.replace("/", " ").split()
        if len(date_list) != 3:
            continue
        month = date_list[0]
        day = date_list[1]
        year = date_list[2]
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        print(f"{year}-{month}-{day}")
        break
    else:
        continue


#方法2
    def format_date(date_list):
        month = date_list[0]
        day = date_list[1]
        year = date_list[2]
        if month in numbers:
            month = numbers[month]
        month = str(month).zfill(2)
        day = day.zfill(2)
        print(f"{year}-{month}-{day}")

    while True:
        date = input("Date: ")
        if "," in date:
            date_list = date.replace(",", "").split()
            if len(date_list) == 3:
                format_date(date_list)
        elif "/" in date:
            date_list = date.replace("/", " ").split()
            if len(date_list) == 3:
                format_date(date_list)