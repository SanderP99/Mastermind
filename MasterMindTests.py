from MasterMindAsked import (ALL_COLORS,
                             get_nb_black_white_matches,
                             create_combination,
                             any_color_in_combination,
                             all_colors_in_combination,
                             is_sublist_of)

simple_combination = ["red", "green", "blue", "white"]

# Tests for get_nb_black_white_matches(given, guess)
assert get_nb_black_white_matches(["blue", "yellow", "yellow", "blue"], ["blue", "yellow", "blue", "yellow"], 4) == (
2, 2)
assert get_nb_black_white_matches(["yellow", "yellow", "yellow", "yellow"], ["blue", "yellow", "blue", "yellow"],
                                  4) == (2, 0)
assert get_nb_black_white_matches(["red", "yellow", "yellow", "yellow"], ["blue", "yellow", "red", "yellow"], 4) == (
2, 1)
assert get_nb_black_white_matches(["red", "green", "blue", "blue"], ["black", "black", "black", "black"], 4) == (0, 0)
assert get_nb_black_white_matches(["red", "green", "blue", "blue"], ["green", "green", "green", "green"], 4) == (1, 0)
assert get_nb_black_white_matches(["green", "white", "blue", "blue"], ["black", "green", "blue", "blue"], 4) == (2, 1)
assert get_nb_black_white_matches(["green", "white", "blue", "blue"], ["blue", "blue", "red", "red"], 4) == (0, 2)
assert get_nb_black_white_matches(["blue", "blue", "red", "red"], ["blue", "blue", "red", "red"], 4) == (4, 0)
assert get_nb_black_white_matches(["red", "red", "blue", "blue"], ["blue", "blue", "red", "red"], 4) == (0, 4)

combination = create_combination(4)
assert len(combination) == 4

# Test for create_combination(nb_elements)
for i in range(10):
    combination = create_combination(i)
    assert len(combination) == i
    for color in combination:
        assert color in ALL_COLORS

# Tests for any_color_in_combination(any, given)
assert any_color_in_combination(["purple", "red"], simple_combination), True
assert any_color_in_combination(["black", "orange"], simple_combination) == False
assert any_color_in_combination([], simple_combination) == False
assert any_color_in_combination(["purple", "red", 'blue'], simple_combination), True
assert any_color_in_combination(["green", "red"], simple_combination), True
assert any_color_in_combination(["purple"], simple_combination) == False

# Tests for all_colors_in_combination(colors, given)
assert all_colors_in_combination(["red", "green", "yellow"], simple_combination) == False
assert all_colors_in_combination(["red", "green", "white"], simple_combination) == True
assert all_colors_in_combination(["red"], simple_combination) == True
assert all_colors_in_combination([], simple_combination) == True

# Test for create_combination(nb_elements) and
# all_colors_in_combination(colors, given)
for i in range(20):
    assert all_colors_in_combination(create_combination(i), ALL_COLORS)

# Tests for is_sublist_of(sublist, given)
simple_list = [1, 2, 3, 4]
for element in simple_list:
    assert is_sublist_of([element], simple_list) == True
assert not is_sublist_of([5], simple_list)
