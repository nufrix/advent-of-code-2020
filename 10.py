import collections
import copy
import sys
import json
import math

data = [153, 69, 163, 123, 89, 4, 135, 9, 124, 74, 141, 132, 75, 3, 18, 134, 84, 15, 61, 91, 90, 98, 99, 51, 131, 166,
        127, 77, 106, 50, 22, 70, 43, 28, 41, 160, 44, 117, 66, 60, 76, 17, 138, 105, 97, 161, 116, 49, 104, 169, 71,
        100, 16, 54, 168, 42, 57, 103, 1, 32, 110, 48, 12, 143, 112, 82, 25, 81, 148, 133, 144, 118, 80, 63, 156, 88,
        47, 115, 36, 2, 94, 128, 35, 62, 109, 29, 40, 19, 37, 122, 142, 167, 7, 147, 121, 159, 87, 83, 111, 162, 150, 8,
        149]

VARIANTS = set()
VARIANTS_LENGTHS = set()
VARIANTS_DIFFERENCE = []


def prepare_data(data):
    sorted_data = sorted(data)
    sorted_data.append(sorted_data[-1] + 3)
    sorted_data = [0] + sorted_data
    return sorted_data


def find_differences(data):
    differences = []
    for index in range(len(data)):
        if index == len(data) - 1:
            break
        differences.append(data[index + 1] - data[index])

    return differences


def count_differences(data):
    differences_count = collections.defaultdict(int)
    for item in data:
        differences_count[item] += 1
    return differences_count


def find_next_values(current_value, remaining_values):
    next_values = []
    for remaining_value in remaining_values:
        if remaining_value - current_value in {1, 2, 3}:
            next_values.append({'next_value': remaining_value, 'remaining_values': [item for item in remaining_values if item > remaining_value]})
    return next_values


def get_variant(variant, remaining_values):
    if not remaining_values or all([remaining_value <= variant[-1] for remaining_value in remaining_values]):
        if tuple(variant) not in VARIANTS:
            VARIANTS.add(tuple(variant))
            if len(VARIANTS) % 10000 == 0:
                print(len(VARIANTS))
                # with open('10.variants.txt', 'w') as f:
                #     f.write(json.dumps(list(VARIANTS)))
        return

    next_values = find_next_values(variant[-1], remaining_values)
    for next_value in next_values:
        new_variant = copy.deepcopy(variant)
        new_variant.append(next_value['next_value'])
        get_variant(new_variant, next_value['remaining_values'])


def find_all_valid_variants(outlets):
    get_variant([0], outlets)


def test_variants():
    data = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    find_all_valid_variants(prepare_data(data)[1:])
    assert len(VARIANTS) == 19208


def find_next_values_difference(current_value, remaining_values):
    pass


def get_variant_difference(variant_difference, remaining_values_difference):
    pass


def find_all_valid_variants_difference(outlets):
    differences = find_differences(outlets)
    print(outlets)
    print(differences)


if __name__ == '__main__':
    if 'test' in sys.argv:
        test_variants()
    else:
        differences = find_differences(prepare_data(data))
        difference_count = count_differences(differences)
        print(difference_count[1] * difference_count[3])
        find_all_valid_variants(data)
        # print(len(VARIANTS))
        print(VARIANTS_LENGTHS)
        # find_all_valid_variants_difference(prepare_data(data)[:-1])
