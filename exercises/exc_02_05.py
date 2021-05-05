from rich import print
from rich import inspect

def mean(numbers):
    """Compute the arithmetic mean of the values in numbers."""
    # add the numbers together
    numbers_sum = sum(numbers)
    # count the values in numbers
    numbers_count = len(numbers)
    # compute the arithmetic mean
    arithmetic_mean = numbers_sum / numbers_count
    return arithmetic_mean

# create a list of numbers
numbers_one = [1, 3, 5, 7]
print("Inspecting the list! :mag:")
inspect(numbers_one, methods=True)
# calculate the mean
print("Computing the mean! :rocket:")
numbers_one_mean = mean(numbers_one)
print(f"Mean: {numbers_one_mean}")
