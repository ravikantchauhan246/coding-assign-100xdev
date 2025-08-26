def square(number):
    """Calculate the number of grains on a specific square."""
    # The tests require an error for numbers outside the 1-64 range.
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
        
    # The number of grains on square 'n' is 2^(n-1).
    return 2**(number - 1)


def total():
    """Calculate the total number of grains on the chessboard."""
    # The sum of grains on all 64 squares is 2^64 - 1.
    return 2**64 - 1