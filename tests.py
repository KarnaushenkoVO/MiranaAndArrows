from mirana_and_arrows import solve_mirana_challenge

ERROR_MESSAGE = 'Assertion failed for {case} case. Expected: {expected}, actual: {actual}'


def test_1_from_description():
    maximum_cumulative_distance = 3
    distances = [1, 2, 3]

    case = '1 from description'
    expected_max_number_of_arrows = 2

    max_number_of_arrows = solve_mirana_challenge(maximum_cumulative_distance, distances)
    assert max_number_of_arrows == expected_max_number_of_arrows, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_number_of_arrows,
        actual=max_number_of_arrows
    )


def test_2_from_description():
    maximum_cumulative_distance = 7
    distances = [5, 4, 2, 2, 3]

    case = '2 from description'
    expected_max_number_of_arrows = 3

    max_number_of_arrows = solve_mirana_challenge(maximum_cumulative_distance, distances)
    assert max_number_of_arrows == expected_max_number_of_arrows, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_number_of_arrows,
        actual=max_number_of_arrows
    )


def test_negative_distance():
    maximum_cumulative_distance = 7
    distances = [5, 4, 2, -2, 3]

    case = 'negative distance'
    expected_max_number_of_arrows = 3

    max_number_of_arrows = solve_mirana_challenge(maximum_cumulative_distance, distances)
    assert max_number_of_arrows == expected_max_number_of_arrows, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_number_of_arrows,
        actual=max_number_of_arrows
    )


def test_edge_case_min_1():
    maximum_cumulative_distance = 1
    distances = [1]

    case = '1 min edge'
    expected_max_number_of_arrows = 1

    max_number_of_arrows = solve_mirana_challenge(maximum_cumulative_distance, distances)
    assert max_number_of_arrows == expected_max_number_of_arrows, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_number_of_arrows,
        actual=max_number_of_arrows
    )


def test_edge_case_min_2():
    maximum_cumulative_distance = 1
    distances = [2]

    case = '2 min edge'
    expected_max_number_of_arrows = 0

    max_number_of_arrows = solve_mirana_challenge(maximum_cumulative_distance, distances)
    assert max_number_of_arrows == expected_max_number_of_arrows, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_number_of_arrows,
        actual=max_number_of_arrows
    )


def test_edge_case_max():
    maximum_cumulative_distance = int(1E9)
    distances = [1, 3, 4, 5, int(1E8)] + ([int(1E9)] * 9995)

    case = 'max edge'
    expected_max_number_of_arrows = 5

    max_number_of_arrows = solve_mirana_challenge(maximum_cumulative_distance, distances)
    assert max_number_of_arrows == expected_max_number_of_arrows, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_number_of_arrows,
        actual=max_number_of_arrows
    )


if __name__ == '__main__':
    test_1_from_description()
    test_2_from_description()
    test_negative_distance()
    test_edge_case_min_1()
    test_edge_case_min_2()
    test_edge_case_max()
