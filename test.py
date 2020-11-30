from kabuka import is_numeric, get_latest_price


def test_is_numeric():
    assert not is_numeric("abc")
    assert not is_numeric("123a")
    assert not is_numeric("")
    assert not is_numeric("this is not a number")
    assert not is_numeric("a123")
    assert not is_numeric("a123a")
    assert not is_numeric("1a123")
    assert not is_numeric("0.0.0.0")
    assert not is_numeric("1,234.678")
    assert is_numeric("123")
    assert is_numeric(".123")
    assert is_numeric("123.")
    assert is_numeric("123.456")
    assert is_numeric("123_456")
    assert is_numeric("0.123")
    assert is_numeric(".123_456")
    assert is_numeric("123_456.")
    assert is_numeric("123_456.789_101")


def test_get_lastest_price():
    # stonk
    price = get_latest_price("TSLA")
    assert is_numeric(price) and float(price) >= 0

    # lower case
    price = get_latest_price("aapl")
    assert is_numeric(price) and float(price) >= 0

    # ETFs
    price = get_latest_price("SPY")
    assert is_numeric(price) and float(price) >= 0

    price = get_latest_price("RWR")
    assert is_numeric(price) and float(price) >= 0

    # tokyo stock exchange
    price = get_latest_price("4385.T")
    assert is_numeric(price) and float(price) >= 0

    # invalid symbol
    try:
        price = get_latest_price("")
    except ValueError:
        assert True
    else:
        assert False

    # invalid symbol
    try:
        price = get_latest_price("apple.com")
    except ValueError:
        assert True
    else:
        assert False



