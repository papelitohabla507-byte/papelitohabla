from datetime import date

import pytest

from apps.documentos.numero_unico import es_numero_valido, generar_numero_unico


def test_genera_formato_correcto():
    numero = generar_numero_unico("mef", "sg", 25, date(2027, 2, 8))
    assert numero == "MEF-SG-2027-000025"


def test_consecutivo_invalido():
    with pytest.raises(ValueError):
        generar_numero_unico("MEF", "SG", 0)


def test_codigo_invalido():
    with pytest.raises(ValueError):
        generar_numero_unico("M1", "SG", 1)


def test_validacion():
    assert es_numero_valido("MINSA-DAJ-2027-000001")
    assert not es_numero_valido("MINSA-2027-1")
