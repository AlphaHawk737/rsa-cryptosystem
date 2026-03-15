from src.prime_generation import is_prime, generate_prime

def test_prime_detection():
    assert is_prime(7)  # known prime
    assert is_prime(97)  # another known prime

def test_non_prime_detection():
    assert not is_prime(9)  # 9 is composite
    assert not is_prime(100)  # 100 is composite

def test_generate_prime():
    p = generate_prime(50, 200)  # random prime generation
    assert is_prime(p)

def test_generate_prime_range():
    p = generate_prime(100, 200)
    assert 100 <= p <= 200  # prime within requested bounds