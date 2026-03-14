def modular_exponentiation(base, exponent, modulus):
    """Calculate (base^exponent) mod modulus using modular exponentiation."""
    result = 1
    base = base % modulus  # Handle cases where base >= modulus

    while exponent > 0:
        # If exponent is odd, multiply base with result
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        
        # Now exponent must be even
        exponent = exponent >> 1  # Equivalent to exponent //= 2
        base = (base * base) % modulus  # Square the base

    return result