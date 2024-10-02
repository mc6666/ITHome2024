from unittest.mock import Mock

values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

mock = Mock()

# side_effect 設為函數
mock.side_effect = side_effect
print(mock('a'), mock('b'), mock('c'))

# side_effect 設為list
mock.side_effect = [5, 4, 3, 2, 1]
print(mock(), mock(), mock())