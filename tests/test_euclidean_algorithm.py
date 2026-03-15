from src.euclidean_algorithm import extended_euclidean_algorithm, modular_inverse

def test_gcd_computation():
    gcd, _, _ = extended_euclidean_algorithm(30, 12)  # compute gcd for sample values
    assert gcd == 6

def test_modular_inverse_valid():
    inv = modular_inverse(17, 3120)  # inverse should exist for coprime inputs
    assert (17 * inv) % 3120 == 1

def test_modular_inverse_small():
    inv = modular_inverse(3, 11)  # manual known inverse
    assert inv == 4

def test_modular_inverse_invalid():
    try:
        modular_inverse(6, 9)  # gcd(6,9)=3 so inverse should fail
        assert False
    except ValueError:
        assert True