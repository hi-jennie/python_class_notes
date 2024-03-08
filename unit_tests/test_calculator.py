from calculator import square

"""

def main():
    test_square1()
    test_square()
    
    
def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
        
def test_square1():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
        
        
if __name__ =="__main__":
    main()
"""


# 用pytest进行测试到第二部就出错了便不会再执行后面的部分，无法弄清哪个部分出了问题
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


# 分城几个不同的部分，用pytest进行曾是可以知道错误究竟出在哪个部分
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_0():
    assert square(0) == 0


# ？def test_str():
#    with pytest.raises(TypeError):
#        square("cat")
