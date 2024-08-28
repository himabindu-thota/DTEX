import pytest

def my_add(a, b):
    return a+b

@pytest.mark.parametrize("input, output", [     
                                            ([1,2],3), 
                                            ([10,12], 22), 
                                            ([1,12], 13), 
                                            ([1,13], 14), 
                                            ([1,14], 15) 
                                            ])
def test_my_add(input, output):
    assert my_add(input[0], input[1]) == output
