from hello import hello


def test_argument():
    for name in ["Jennie", "Rustin"]:
        assert hello(name) == f"hello,{name}"
    # 可以通过loop多测试几个值，但是如果测试代码很复杂我们又得保证测试代码的正确性，所以测试代码尽量简单。


def test_default():
    assert hello() == "hello,world"
