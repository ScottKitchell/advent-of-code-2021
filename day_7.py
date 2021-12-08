import day_7_data as DATA


# PART 1
def fuel_to_align_1(positions):
  min_fuel_cost = float('inf')

  for target_pos in range(max(positions) + 1):
    fuel_cost = 0
    for pos in positions:
      dist = abs(target_pos - pos)
      fuel_cost += dist

    if fuel_cost < min_fuel_cost:
      min_fuel_cost = fuel_cost

  print(min_fuel_cost)
  return min_fuel_cost


# PART 2
def fuel_to_align_2(positions):
  min_fuel_cost = float('inf')

  for target_pos in range(max(positions) + 1):
    fuel_cost = 0
    for pos in positions:
      dist = abs(target_pos - pos)
      fuel_cost += triangular_num(dist)

    if fuel_cost < min_fuel_cost:
      min_fuel_cost = fuel_cost

  print(min_fuel_cost)
  return min_fuel_cost


def triangular_num(num):
  """ Sums all numbers from `0` to `num` """
  return round((num * (num + 1) / 2))


def run_tests(function, test_data):
  for positions, expected_val in test_data:
    val = function(positions)
    assert val == expected_val, \
      "{}: {} does not equal {}".format(function.__name__, val, expected_val)


if __name__ == '__main__':
  print('Testing...')
  run_tests(fuel_to_align_1, DATA.TESTS_1)
  run_tests(fuel_to_align_2, DATA.TESTS_2)
  print('Testing complete')

  fuel_to_align_1(DATA.POSITIONS)
  fuel_to_align_2(DATA.POSITIONS)  # 96987874
