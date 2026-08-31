print("Oleksandr Romaniuk, IT-31");

day = int(input("Enter your birthday day (integer): "));
month = int(input("Enter your birthday month (integer): "));
year = int(input("Enter your birthday year (integer): "));

if 13 > month > 0:
    if year > 0:
        if month in (1, 3, 5, 7, 8, 10, 12):
            if 32 > day > 0:
                validity = "Date is valid";
            else:
                validity = f"Date is invalid: month {month} has only 31 days";
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if 30 > day > 0:
                    validity = "Date is valid";
                else:
                    validity = f"Date is invalid: month {month} has only 29 days";
            else: 
                if 29 > day > 0:
                    validity = "Date is valid";
                else:
                    validity = f"Date is invalid: month {month} has only 28 days";
        else: 
            if 31 > day > 0:
                validity = "Date is valid";
            else:
                validity = f"Date is invalid: month {month} has only 30 days";
    else:
        validity = f"Date is invalid: year can be only positive";
else:
    validity = f"Date is invalid: month can be only up to 12";

print(validity)