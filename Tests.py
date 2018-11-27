import nose
import Source

dst_points = [[85, 1163], [686, 1163], [686, 77], [82, 64], [82, 226], [244, 64]]

def test_initial():
  assert dst_points[:] == dst_points[:]

def test_top():
  assert Source.isTop([100,100])
  assert not Source.isTop([100,700])

def test_left():
  assert Source.isLeft([100,100])
  assert not Source.isLeft([400,100])