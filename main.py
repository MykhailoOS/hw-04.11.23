# Task1
def generator_mul(stop):

    num = 2
    while num < stop:
        yield num
        num *= 2


for i in generator_mul(20):
    print(i)

# Task2
def generator_range(start, stop, step):
    while 0 < start < stop:
        yield start
        start *= step


for i in generator_range(2, 10, 3):
    print(i)

# Task3
def simple_num_generator(start, stop):
    while 0 < start < stop:
        yield start
        start += 1


for i in simple_num_generator(2, 997):
    if i % 2 != 0 and i // i and i % 3 != 0:
        print(i)

# Task4
gen_list = []


def generator_range(start):
    while start < 10000:
        yield start
        start = start ** 3


for i in generator_range(2):
    gen_list.append(i)
print(gen_list)


# Task5 розбиралили на уроці


# Task6
def simple_num_generator(start_date, stop_date):
    while 0 < start_date < stop_date:
        yield start_date
        start_date += 1


for i in simple_num_generator(1.11, 30.11):
    print(f"дата: {i:.2f} 2020")
