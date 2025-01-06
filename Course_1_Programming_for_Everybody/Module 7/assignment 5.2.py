def main():
    largest = None
    smallest = None

    while True:
        user_input = input("Enter a number: ")
        if user_input == 'done':
            break
        try:
            number = int(user_input)
        except ValueError:
            print("Invalid input")
            continue

        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number

    print("Maximum is", largest)
    print("Minimum is", smallest)

main()
