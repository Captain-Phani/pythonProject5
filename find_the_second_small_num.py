def second_minimum_negative(numbers):
    if len(numbers) < 2:
        return "List should contain at least two elements"

    min_num = None
    second_min = None

    for num in numbers:
        if min_num is None or num < min_num:
            second_min = min_num
            min_num = num
        elif num != min_num and (second_min is None or num < second_min):
            second_min = num

    return second_min if second_min is not None else "No second minimum found"


# Example usage:
elements = [1,7,-8,-1,10]
print("Second minimum:", second_minimum_negative(elements))