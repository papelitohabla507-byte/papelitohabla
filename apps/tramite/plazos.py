"""Cálculo de fechas límite y alertas de vencimiento (HU-17)."""
from datetime import timedelta


def sumar_dias_habiles(inicio, dias):
    """Suma días hábiles (lunes a viernes) a una fecha."""
    actual = inicio
    restantes = dias
    while restantes > 0:
        actual += timedelta(days=1)
        if actual.weekday() < 5:
            restantes -= 1
    return actual


def estado_plazo(fecha_limite, hoy, dias_alerta=2):
    """Devuelve 'vencido', 'por_vencer' o 'a_tiempo'."""
    if hoy > fecha_limite:
        return "vencido"
    if (fecha_limite - hoy).days <= dias_alerta:
        return "por_vencer"
    return "a_tiempo"
