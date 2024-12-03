from src.math_operation import add,sub

def test_add():
    assert add(3,5)==8
    assert add(5,6)==11
    assert add(-1,-1)==0

def test_sub():
    assert sub(5,4)==1
    assert sub(7,3)== -4 
    assert(4,4)==0