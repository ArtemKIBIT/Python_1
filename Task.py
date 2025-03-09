def is_even(n):
    return n % 2 == 0

def product_of_even_numbers(n):
    product = 1
    for i in range(2, n + 1, 2):
        product *= i
    return product

def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {n * i}")
    return "\n".join(table)

def main():
    try:
        n = int(input("Введіть число: "))
        if is_even(n):
            print(f"Число {n} є парним.")
        else:
            print(f"Число {n} є непарним.")
        product = product_of_even_numbers(n)
        print(f"Добуток всіх парних чисел від 1 до {n}: {product}")
        print("Таблиця множення для", n)
        print(multiplication_table(n))

    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()