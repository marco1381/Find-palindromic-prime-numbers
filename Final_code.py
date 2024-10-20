# Reference
""" OpenAI (2022). ChatGPT. [online]. Available at: https://chat.openai.com/
(Accessed: 12th March 2024). """
# Date: [19/03/2024]
# Name: Marco Gizzi
# ID: 001327359

# Import necessary modules
import timeit  # Module for measuring time


# Function to find prime numbers
def prime_number(num):
    # Check if the number is less than 2, numbers less than 2 are not prime
    if num < 2:
        return False
    # 2 is the only even prime number
    if num == 2:
        return True
    # Check if the number is even, excluding 2
    if num % 2 == 0:
        return False
    # Iterates from 2 to the square root of the number
    '''Used OpenAI (2022) to generate int(num ** 0.5)'''
    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible evenly by i, it is not prime
        if num % i == 0:
            return False
    # Return prime numbers
    return True


# Function to find palindromic prime numbers
def palindromic_primes(m, n):
    palindromic_prime_num = set()  # Empty set to store palindromic primes
    # Iterates in range 1 to n
    for i in range(1, n + 1):
        str_i = str(i)  # Convert the value to a string
        # Palindromes generation by joining the string with its reverse
        '''Used OpenAI (2022) to generate the following line'''
        palindrome_num = int(''.join([str_i, str_i[-2::-1]]))
        # Break the loop if the palindromes exceeds the n value
        if palindrome_num > n:
            break
        # Check if the palindromes in the given range are prime numbers
        if m <= palindrome_num <= n and prime_number(palindrome_num):
            palindromic_prime_num.add(palindrome_num)
    # Convert the set to a sorted list and return it
    return sorted(palindromic_prime_num)


# Main block of code
if __name__ == "__main__":
    try:
        # Inputs from the user
        first_input = int(input("Enter first value: "))
        second_input = int(input("Enter second value: "))
        # Constrains the first input to be smaller than the second
        if first_input > second_input:
            print("The first input has to be smaller than the second input.")
        else:
            # Measure execution time using timeit
            start_time = timeit.default_timer()
            # Special case for second input <= 11
            if second_input <= 11:
                # Find palindromic primes in range first input and second input
                special_numbers = palindromic_primes(first_input, second_input)
            # Special case for first input <= 11
            elif first_input <= 11:
                # Find palindromic primes in range first input and second input
                special_numbers = palindromic_primes(first_input, second_input)
                # Add 11 if the first input <= 11
                special_numbers.append(11)
                special_numbers.sort()  # Sort the results
            else:
                # Find palindromic primes in range first input and second input
                special_numbers = palindromic_primes(first_input, second_input)
            # Displays special numbers result
            if len(special_numbers) <= 5:
                print(f"All {len(special_numbers)} are special numbers: {special_numbers}")
            else:
                # Displays the first and last 3 special numbers
                first_three = special_numbers[:3]
                last_three = special_numbers[-3:]
                print(f"First three special numbers {first_three}")
                print(f"Last three special numbers {last_three}")
            # Displays the total special numbers
            print(f"All special numbers: {len(special_numbers)}")
            end_time = timeit.default_timer()
            # Displays time taken
            print(f"Time taken: {end_time - start_time} seconds")
    except KeyboardInterrupt:
        print("\nExiting Simulation")
