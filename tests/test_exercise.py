import pytest
import src.exercise

def test_exercise():
    input_values = ["11","4","5","64","-1","4","11","5","5","64","-1","5","11","5","5","64","-1","12"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["","","","","","Search for?","4 is at index 1",\
                        "","","","","","Search for?","5 is at index 1","5 is at index 2",\
                        "","","","","","Search for?"]
