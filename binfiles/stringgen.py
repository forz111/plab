import random


def write_random_to_file(num_lines):
    product_names = ['Apple', 'Banana', 'Cherry', 'Milk', 'Sugar', 'Bread']
    prices = [100, 150, 400, 250, 700, 200, 300]
    discounts = [True, False]

    with open('product_info.txt', 'w') as f:
        for _ in range(num_lines):
            f.write(f"{random.choice(product_names)} ")
            f.write(f"{str(random.choice(prices))} ")
            f.write(f"{str(random.choice(discounts))}\n")


write_random_to_file(15)
