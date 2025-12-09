
import string
import random


# ------------------------------------------------------------
#              Generador simple de códigos cortos
#    Creamos cadenas aleatorias alfanuméricas de longitud 6
#      Más adelante se podrá usar hash real, base62, etc.
# ------------------------------------------------------------

def generate_short_code(length: int = 6) -> str:
    """
    Genera un código corto aleatorio usando letras y números.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
