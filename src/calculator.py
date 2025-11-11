def add(a, b):
    """Addition de deux nombres
    
    Cette fonction additionne a et b.
    
    Args:
        a: Premier nombre à additionner
        b: Deuxième nombre à additionner
    
    Returns:
        La somme de a et b
    """
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """Division de a par b
    
    Args:
        a: Le numérateur
        b: Le dénominateur
    
    Returns:
        Le résultat de a / b
    
    Raises:
        ZeroDivisionError: Si b vaut 0
    """
    if b == 0:
        raise ZeroDivisionError("Erreur : impossible de diviser par zéro")
    result = a / b
    return result
