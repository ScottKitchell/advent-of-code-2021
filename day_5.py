import day_5_data as DATA

SPACE = 1000


def run_tests(function, test_data):
  for data, expected_val in test_data:
    val = function(data)
    assert val == expected_val, \
      "{}: {} does not equal {}".format(function.__name__, val, expected_val)


def limited_danger_score(coordinates):
  """ Only considers horizontal and vertical lines. """
  is_horizontal = lambda start, end: start[0] == end[0]
  is_vertical = lambda start, end: start[1] == end[1]
  point_counters = {}

  def mark_point(x, y):
    key = f"{x}|{y}"
    point_counters.setdefault(key, 0)
    point_counters[key] += 1

  for start, end in coordinates:
    if is_horizontal(start, end):
      x = start[0]
      step = 1 if end[1] >= start[1] else -1
      for y in range(start[1], end[1] + step, step):
        mark_point(x, y)
    elif is_vertical(start, end):
      y = start[1]
      step = 1 if end[0] >= start[0] else -1
      for x in range(start[0], end[0] + step, step):
        mark_point(x, y)

  return score_danger(point_counters)


def danger_score(coordinates):
  """ Considers horizontal, vertical and diagonal lines. """
  is_horizontal = lambda start, end: start[0] == end[0]
  is_vertical = lambda start, end: start[1] == end[1]
  point_counters = {}

  def mark_point(x, y):
    key = f"{x}|{y}"
    point_counters.setdefault(key, 0)
    point_counters[key] += 1

  def mark_horizontal(start, end):
    x = start[0]
    step = 1 if end[1] >= start[1] else -1
    for y in range(start[1], end[1] + step, step):
      mark_point(x, y)

  def mark_vertical(start, end):
    y = start[1]
    step = 1 if end[0] >= start[0] else -1
    for x in range(start[0], end[0] + step, step):
      mark_point(x, y)

  def mark_diagonal(start, end):
    x = start[0]
    y = start[1]
    x_step = 1 if end[0] >= start[0] else -1
    y_step = 1 if end[1] >= start[1] else -1
    length = abs(end[0] - start[0]) + 1
    for i in range(length):
      mark_point(x, y)
      x += x_step
      y += y_step

  for start, end in coordinates:
    if is_horizontal(start, end):
      mark_horizontal(start, end)
    elif is_vertical(start, end):
      mark_vertical(start, end)
    else:
      mark_diagonal(start, end)

  return score_danger(point_counters)
    
 
def score_danger(point_counts):
  counter = 0
  for point in point_counts.values():
    if point >= 2:
      counter += 1

  print("score", counter)
  return counter

        
if __name__ == '__main__':
  print('Testing...')
  run_tests(limited_danger_score, DATA.LIMITED_TESTS)
  run_tests(danger_score, DATA.TESTS)
  print('Testing complete')

  limited_danger_score(DATA.COORDINATES)
  danger_score(DATA.COORDINATES)
