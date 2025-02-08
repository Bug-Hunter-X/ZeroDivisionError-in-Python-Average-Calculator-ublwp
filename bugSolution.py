def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage with potential error:
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

#Improved Solution with better error handling
def calculate_average_improved(numbers):
    if not numbers:
        return 0
    try:
        return sum(numbers) / len(numbers)
    except TypeError as e:
        print(f"Error calculating average: {e}")
        return None #or raise the exception