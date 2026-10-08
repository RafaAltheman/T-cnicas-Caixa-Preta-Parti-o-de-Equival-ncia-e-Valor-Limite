
import pytest

from codigo import (
    calcular_imc,
    categorizar_imc,
    classificar_pessoa,
    classificar_por_faixas,
    classificar_vento,
    tem_frete_gratis,
    FAIXAS_VENTO,
)

@pytest.mark.parametrize(
    "peso, altura, esperado",
    [
        (50, 1.70, "abaixo do peso"),
        (65, 1.70, "peso normal"),
        (80, 1.70, "sobrepeso"),
        (100, 1.70, "obesidade"),
    ],
    ids=[
        "abaixo-do-peso",
        "peso-normal",
        "sobrepeso",
        "obesidade",
    ],
)
def test_classes_imc(peso, altura, esperado):
    assert classificar_pessoa(peso, altura) == esperado

@pytest.mark.parametrize(
    "imc, esperado",
    [
        (18.49, "abaixo do peso"),
        (18.50, "peso normal"),
        (18.51, "peso normal"),
        (24.99, "peso normal"),
        (25.00, "sobrepeso"),
        (25.01, "sobrepeso"),
        (29.99, "sobrepeso"),
        (30.00, "obesidade"),
        (30.01, "obesidade"),
    ],
    ids=[
        "18.5-abaixo",
        "18.5-limite",
        "18.5-acima",
        "25-abaixo",
        "25-limite",
        "25-acima",
        "30-abaixo",
        "30-limite",
        "30-acima",
    ],
)
def test_limites_imc(imc, esperado):
    assert categorizar_imc(imc) == esperado

@pytest.mark.parametrize(
    "peso, altura",
    [
        (0, 1.70),
        (70, 0),
    ],
    ids=["peso-invalido", "altura-invalida"],
)
def test_imc_invalido(peso, altura):
    with pytest.raises(ValueError):
        calcular_imc(peso, altura)


@pytest.mark.parametrize(
    "velocidade, esperado",
    [
        (10, "calmo"),
        (30, "moderado"),
        (50, "forte"),
        (70, "tempestade"),
    ],
    ids=["calmo", "moderado", "forte", "tempestade"],
)
def test_classes_vento(velocidade, esperado):
    resultado = classificar_por_faixas(
        velocidade, FAIXAS_VENTO
    )
    assert resultado == esperado
    assert classificar_vento(velocidade) == esperado


@pytest.mark.parametrize(
    "velocidade, esperado",
    [
        (19.9, "calmo"),
        (20, "moderado"),
        (20.1, "moderado"),
        (39.9, "moderado"),
        (40, "forte"),
        (40.1, "forte"),
        (59.9, "forte"),
        (60, "tempestade"),
        (60.1, "tempestade"),
    ],
    ids=[
        "20-abaixo",
        "20-limite",
        "20-acima",
        "40-abaixo",
        "40-limite",
        "40-acima",
        "60-abaixo",
        "60-limite",
        "60-acima",
    ],
)
def test_limites_vento(velocidade, esperado):
    resultado = classificar_por_faixas(
        velocidade, FAIXAS_VENTO
    )
    assert resultado == esperado

@pytest.mark.parametrize(
    "valor, premium, peso, esperado",
    [
        (200, True, 30, True),    # R1
        (200, True, 31, False),   # R2
        (200, False, 30, False),  # R3
        (200, False, 31, False),  # R4
        (199, True, 30, False),   # R5
        (199, True, 31, False),   # R6
        (199, False, 30, False),  # R7
        (199, False, 31, False),  # R8
    ],
    ids=[
        "R1", "R2", "R3", "R4",
        "R5", "R6", "R7", "R8",
    ],
)
def test_frete_gratis(valor, premium, peso, esperado):
    resultado = tem_frete_gratis(valor, premium, peso)
    assert resultado is esperado
