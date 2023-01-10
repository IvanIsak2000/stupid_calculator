print("программа расчёта зарплаты")
file = open('my_pay.txt')

try:
    for string in file:
        string = string.rstrip()
        if string.startswith("pay"):
            pay = float(string[4::])
        if string.startswith("hours"):
            hours = float(string[6::])
        if string.startswith("limit"):
            limit = float(string[6::])
        if string.startswith("stavka"):
            stavka = float(string[7::])

    if hours <= limit:  # <40
        def function(pay, hours):
            count = pay * hours
            return count
            pass


        x = function(pay, hours)
        print(x)

        print("зарплата ", pay)
        print("часы работы ", hours)
        print("лимит часов ", limit)

    elif hours > limit:  # 60>50

        def переработка(pay, hours):
            счёт = float(((hours - limit) * (pay * stavka) + (limit * pay)))
            return счёт
            pass
        x = переработка(pay, hours)
        print(x)
        print("зарплата ", pay)
        print("часы работы ", hours)
        print("лимит часов ", limit)
        print("ставка ", stavka)
except:
    print("ОШИБКА")
#пример заполнения файла my_pay.txt:#
#pay:0000#
#hours:000#
#limit:000#
#stavka:00#
