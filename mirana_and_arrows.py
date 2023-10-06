PARSING_ERROR_MESSAGE = 'Invalid format. Please check example of usage in the documentation (README.md)'


def parse_numbers(raw_numbers):
    """
       Utility function to parse input line

       :param str raw_numbers: Space separated numbers. Example: '3 4 5'
       :return: Parsed numbers, compacted into list. Example: [3, 4, 5]
       :rtype: list[int, ...]
       :raises ValueError: If format of string cannot be parsed into integer numbers
    """
    try:
        return list(map(int, raw_numbers.split(' ')))
    except Exception:
        raise ValueError(PARSING_ERROR_MESSAGE)


def solve_mirana_challenge(maximum_cumulative_distance, distances):
    """
       Main function, which incorporates the logic of finding maximum number of arrows for mirana.

       :param int maximum_cumulative_distance: Max distance for Mirana until perish. Example: 3
       :param list[int, ...] distances: Max distance for each arrow. Example: [1, 2, 3]
       :return: max number of arrows for Mirana within max cumulative distance constraint. Example: 2
       :rtype: int
    """

    max_number_of_arrows = 0

    for pivot_distance_id in range(len(distances)):  # Let's try to use every arrow as a starting point
        _local_sum = 0
        _current_number_of_arrows = 0

        # Sum all distances from starting arrow util it exceeds maximum_cumulative_distance
        for distance_to_sum in distances[pivot_distance_id:]:
            _new_local_sum = _local_sum + abs(distance_to_sum)  # Consider only positive distances
            if _new_local_sum <= maximum_cumulative_distance:
                _local_sum = _new_local_sum
                _current_number_of_arrows += 1
            else:
                break

        # If on some iteration we used more arrows than before, let's save it as a max number
        if _current_number_of_arrows > max_number_of_arrows:
            max_number_of_arrows = _current_number_of_arrows

    return max_number_of_arrows


# Let's separate input/output logic and domain logic to cover domain logic with tests in another module
if __name__ == '__main__':
    print('Please enter input parameters accordingly to documentation')
    # Read numbers of arrows and maximum cumulative distance
    num_arrows, max_cumulative_distance = parse_numbers(input())

    # Loop to read max distance for each arrow
    dists = parse_numbers(input())  # We assume that distance can be only positive to have physical interpretation

    # Main function which solves Mirana's problem
    max_number_of_arrows_for_mirana = solve_mirana_challenge(max_cumulative_distance, dists)
    print(max_number_of_arrows_for_mirana)
