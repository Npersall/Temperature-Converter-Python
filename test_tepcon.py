from tempcon import TempConverter

def test_freezing_fahrenhieht():

    actual = TempConverter().to_celsius(32.0)
    expected = 0.0

    assert abs(expected - actual) < 0.01

def test_freezing_celsius():

    converter = TempConverter()

    actual = converter.to_fahrenheiht(0.0)
    expected = 32.0

    assert abs(expected - actual) < 0.01
    assert abs(expected - actual) > -0.01