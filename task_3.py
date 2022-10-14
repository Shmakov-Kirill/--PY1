money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
canLive = True
while canLive:
    money_capital += salary - spend
    spend += spend * increase
    month += 1
    if money_capital + salary < spend:
        canLive = False

print(month)
