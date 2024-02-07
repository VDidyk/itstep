# Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними

def sum_of_range(start, end):
    total = sum(range(start, end + 1))
    return total


start = int(input("Enter the first number: "))
end = int(input("Enter the last number: "))
result = sum_of_range(start, end)
print("The result is:", result)
