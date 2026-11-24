from datetime import date

from apps.tramite.plazos import estado_plazo, sumar_dias_habiles


def test_salta_fin_de_semana():
    # viernes 12/02/2027 + 1 día hábil = lunes 15/02/2027
    assert sumar_dias_habiles(date(2027, 2, 12), 1) == date(2027, 2, 15)


def test_estados_del_plazo():
    limite = date(2027, 3, 10)
    assert estado_plazo(limite, date(2027, 3, 1)) == "a_tiempo"
    assert estado_plazo(limite, date(2027, 3, 9)) == "por_vencer"
    assert estado_plazo(limite, date(2027, 3, 11)) == "vencido"
