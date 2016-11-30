

def test_open_baidu(driver_mock, bd):
    bd.open_baidu()
    assert driver_mock.get.called
