from copy import deepcopy
import day_6_data as DATA

BIRTHING_FISH = 0
NEW_FISH = 8
RESET_FISH = 6
DAYS_80 = 80
DAYS_256 = 80


def model_fish_population_1(initial_fish, days_to_monitor):
  fish = deepcopy(initial_fish)  # so we can mutate it

  for day in range(days_to_monitor):
    for i in range(len(fish)):
      if fish[i] == BIRTHING_FISH:
        fish.append(NEW_FISH)
        fish[i] = RESET_FISH
      else:
        fish[i] -= 1

  fish_count = len(fish)
  print("fish count", fish_count)
  return fish_count


def model_fish_population_2(initial_fish, days_to_monitor):
  fish_counts = [0 for i in range(9)]  # 0 - 8
  for stage in initial_fish:
    fish_counts[stage] += 1

  for day in range(days_to_monitor):
    birthing_fish_count = fish_counts.pop(BIRTHING_FISH)
    fish_counts.append(birthing_fish_count)
    fish_counts[RESET_FISH] += birthing_fish_count

  fish_count = sum(fish_counts)
  print("fish count", fish_count)
  return fish_count


def run_tests(function, test_data):
  for fish, days, expected_val in test_data:
    val = function(fish, days)
    assert val == expected_val, \
      "{}: {} does not equal {}".format(function.__name__, val, expected_val)


if __name__ == '__main__':
  print('Testing...')
  run_tests(model_fish_population_1, DATA.TESTS_1)
  run_tests(model_fish_population_2, DATA.TESTS_2)
  print('Testing complete')

  model_fish_population_1(DATA.INITIAL_FISH, DAYS_80)
  model_fish_population_2(DATA.INITIAL_FISH, DAYS_256)
