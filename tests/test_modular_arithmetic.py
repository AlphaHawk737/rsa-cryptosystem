from src.modular_arithmetic import modular_exponentiation

def test_modular_exponentiation_basic():
    assert modular_exponentiation(2, 5, 13) == pow(2, 5, 13)  # basic exponentiation

def test_modular_exponentiation_large():
    assert modular_exponentiation(65, 17, 3233) == pow(65, 17, 3233)  # verify with known RSA test

def test_modular_exponentiation_identity():
    assert modular_exponentiation(10, 0, 7) == 1  # exponent 0 should return 1

def test_modular_exponentiation_modulus():
    assert modular_exponentiation(20, 3, 5) == pow(20, 3, 5)  # modulus property