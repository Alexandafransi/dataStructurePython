# prices = [298, 305, 320, 301, 292]
#
# for i in range(len(prices)):
#     if prices[i] == 301:
#         print("${hellow}")

month_exp = [
    {"month": "Jan", "expenses": 2200},
    {"month": "Feb", "expenses": 2350},
    {"month": "Mar", "expenses": 2600},
    {"month": "Apr", "expenses": 2130},
    {"month": "May", "expenses": 2190},
]
spent_extra = 0
counter = 0
first_quarter = 0
for i in range(len(month_exp)):
    counter += 1
    first_quarter += month_exp[i]["expenses"]
    if month_exp[i]["month"] == "Jan":
        spent_extra = month_exp[i]["expenses"]
    if month_exp[i]["month"] == "Feb":
        dollar = month_exp[i]["expenses"] - spent_extra
        print("dollars you spent extra compare to jan", dollar)

    if counter == 3:
        print("Total expenses in first quarter ", first_quarter)

    if month_exp[i]["expenses"] == 2000:
        print("there is a month i spent 2000 dollar")

    if i == len(month_exp) - 1:
        print("this is last element", month_exp[i]["month"])
        month_exp.append({"month": "Jun", "expenses": 1980})

    if month_exp[i]["month"] == "Apr":
        month_exp[i]["expenses"]+= 200
        print("this is correction a refunded",month_exp[i]["expenses"])
