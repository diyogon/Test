import nose
import Source

dst_points = [[85, 1163], [686, 1163], [686, 77], [82, 64], [82, 226], [244, 64]]

def test_initial():
  assert dst_points[:] == dst_points[:]