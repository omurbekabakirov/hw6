counter = 0
while True:
    try:
        num = int(input("Enter number in range 1 to 100: "))

        if num > 100 or num < 1:
            print("Number is not in the range 1 to 100.")
            break

        num_guess = 100 // 2

        try:
            answer = input(f'Your chosen number is {num_guess}. Is it correct? (yes, higher, lower): ')
            counter += 1
            if answer.lower() == "yes":
                with open('game.txt', 'w') as file:
                    file.write(f'{num_guess} is your chosen number. {counter } is  number of attempts')
                print("Game saved. Exiting.")
                break
            elif answer.lower() == "higher":
                num_guess = (num_guess + 100) // 2
                print(num_guess)
                print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                counter += 1
                if answer.lower() == "yes":
                    with open('game.txt', 'w') as file:
                        file.write(f'{num_guess} is your chosen number. {counter} is  number of attempts')
                    print("Game saved. Exiting.")
                    break
                elif answer.lower() == "higher":
                    num_guess = (num_guess + 50 ) // 2
                    print(num_guess)
                    print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                    counter += 1
                    if answer.lower() == "yes":
                        with open('game.txt', 'w') as file:
                            file.write(f'{num_guess} is your chosen number. {counter} is  number of attempts')
                        print("Game saved. Exiting.")
                        break
                    elif answer.lower() == "higher":
                        num_guess = (num_guess + 25) // 2
                        print(num_guess)
                        print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                        counter += 1

                    elif answer.lower() == "lower":
                        num_guess = num_guess // 2
                        print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                        counter += 1
                    else:
                        print("Invalid input. Please enter 'yes', 'higher', or 'lower'.")

                elif answer.lower() == "lower":
                    num_guess = num_guess // 2
                    print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                    counter += 1
                else:
                    print("Invalid input. Please enter 'yes', 'higher', or 'lower'.")

            elif answer.lower() == "lower":
                num_guess = num_guess // 2
                print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): ') )
                counter += 1
                if answer.lower() == "yes":
                    with open('game.txt', 'w') as file:
                        file.write(f'{num_guess} is your chosen number. {counter} is  number of attempts')
                    print("Game saved. Exiting.")
                    break
                elif answer.lower() == "higher":
                    num_guess = (num_guess + 50) // 2
                    print(num_guess)
                    print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                    counter += 1
                    if answer.lower() == "yes":
                        with open('game.txt', 'w') as file:
                            file.write(f'{num_guess} is your chosen number. {counter} is  number of attempts')
                        print("Game saved. Exiting.")
                        break
                    elif answer.lower() == "higher":
                        num_guess = (num_guess + 25) // 2
                        print(num_guess)
                        print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                        counter += 1

                    elif answer.lower() == "lower":
                        num_guess = num_guess // 2
                        print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                        counter += 1
                    else:
                        print("Invalid input. Please enter 'yes', 'higher', or 'lower'.")

                elif answer.lower() == "lower":
                    num_guess = num_guess // 2
                    print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                    counter += 1
                    if answer.lower() == "yes":
                        with open('game.txt', 'w') as file:
                            file.write(f'{num_guess} is your chosen number. {counter} is  number of attempts')
                        print("Game saved. Exiting.")
                        break
                    elif answer.lower() == "higher":
                        num_guess = (num_guess + 25) // 2
                        print(num_guess)
                        print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                        counter += 1

                    elif answer.lower() == "lower":
                        num_guess = num_guess // 2
                        print(input(f'your number is {num_guess} Is it correct?(yes, higher, lower): '))
                        counter += 1
                    else:
                        print("Invalid input. Please enter 'yes', 'higher', or 'lower'.")
                else:
                    print("Invalid input. Please enter 'yes', 'higher', or 'lower'.")


            else:
                print("Invalid input. Please enter 'yes', 'higher', or 'lower'.")

        except ValueError:
            print('Only integer numbers are allowed for the answer.')

    except ValueError:
        print('Only integer numbers are allowed for the chosen number.')