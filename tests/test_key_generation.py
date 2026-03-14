from src.key_generation import generate_rsa_keys
import math

def test_key_generation_structure():
    keys = generate_rsa_keys()

    assert "p" in keys
    assert "q" in keys
    assert "n" in keys
    assert "phi" in keys
    assert "e" in keys
    assert "d" in keys

def test_n_correct():
    keys = generate_rsa_keys()
    assert keys["n"] == keys["p"] * keys["q"]

def test_phi_correct():
    keys = generate_rsa_keys()
    assert keys["phi"] == (keys["p"] - 1) * (keys["q"] - 1)

def test_e_coprime_phi():
    keys = generate_rsa_keys()
    assert math.gcd(keys["e"], keys["phi"]) == 1