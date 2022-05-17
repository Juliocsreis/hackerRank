from datetime import datetime

format = '%I:%M:%S%p'
new_format = '%H:%M:%S'

ex1 = '07:05:45PM'
ex2 = '07:05:45AM'
ex3 = '12:05:45PM'
ex4 = '12:00:00AM'

examples = [ex1, ex2, ex3, ex4]


def timeConversion(s):
    my_date = datetime.strptime(s, format)
    print(my_date.strftime(new_format))


for i in examples:
    timeConversion(i)
