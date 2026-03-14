from src.euclidean_algorithm import extended_euclidean_algorithm, modular_inverse

def test_gcd_computation():
    gcd, _, _ = extended_euclidean_algorithm(30, 12)
    assert gcd == 6

def test_modular_inverse_valid():
    inv = modular_inverse(17, 3120)
    assert (17 * inv) % 3120 == 1

def test_modular_inverse_small():
    inv = modular_inverse(3, 11)
    assert inv == 4

def test_modular_inverse_invalid():
    try:
        modular_inverse(6, 9)
        assert False
    except ValueError:
        assert True