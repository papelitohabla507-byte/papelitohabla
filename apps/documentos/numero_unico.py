"""Generación y validación del número único de documentos (HU-08)."""
import re
from datetime import date

PATRON = re.compile(r"^[A-Z]{2,6}-[A-Z]{2,6}-\d{4}-\d{6}$")


def generar_numero_unico(ministerio, departamento, consecutivo, fecha=None):
    """Devuelve el número único con formato MIN-DEP-AÑO-CONSECUTIVO."""
    if consecutivo < 1:
        raise ValueError("El consecutivo debe ser mayor que cero")
    fecha = fecha or date.today()
    numero = f"{ministerio.upper()}-{departamento.upper()}-{fecha.year}-{consecutivo:06d}"
    if not es_numero_valido(numero):
        raise ValueError(f"Número único inválido: {numero}")
    return numero


def es_numero_valido(numero):
    """Indica si un texto cumple el formato del número único."""
    return bool(PATRON.match(numero))
