def check_palindrome(numbers):
    for n in numbers:
        if n == n[::-1]:
            print("True")
        else:
            print("False")


main_list = input().split(", ")
check_palindrome(main_list)
