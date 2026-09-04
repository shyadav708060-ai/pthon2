def find_odd_numbers(numbers):
    """
    This function takes a list of numbers and returns a list of odd numbers from that list.
    
    :param numbers: List of integers
    :return: List of odd integers
    """
    return [num for num in numbers if num % 2 != 0]

print(find_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [1, 3, 5, 7, 9]