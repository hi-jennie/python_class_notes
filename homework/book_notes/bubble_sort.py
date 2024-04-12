# 默认所有的偶数比奇数大


def magic_bubble_sort(numbers):
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i + 1]
            current_is_even, next_is_even = current % 2 == 0, next_ % 2 == 0
            should_swap = False

            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True

            if should_swap:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                

        stop_position -= 1
        
    print(numbers)


def main():
    numbers = [23, 32, 1, 3, 4, 19, 20, 2, 4]
    magic_bubble_sort(numbers)


main()
