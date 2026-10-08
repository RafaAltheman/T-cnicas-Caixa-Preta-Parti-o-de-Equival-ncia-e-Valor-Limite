
# Laboratório 6 — Técnicas de Caixa-Preta

## Exercício 1 — Partição de Equivalência

Implementação do cálculo e classificação do IMC.

| Classe | Intervalo de IMC | Classificação |
|---|---|---|
| 1 | IMC < 18,5 | Abaixo do peso |
| 2 | 18,5 ≤ IMC < 25 | Peso normal |
| 3 | 25 ≤ IMC < 30 | Sobrepeso |
| 4 | IMC ≥ 30 | Obesidade |

## Exercício 2 — Análise de Valor-Limite

Foram identificadas três fronteiras internas: 18,5, 25 e 30.

| Fronteira | Abaixo | Na fronteira | Acima |
|---|---|---|---|
| 18,5 | 18,49 | 18,50 | 18,51 |
| 25 | 24,99 | 25,00 | 25,01 |
| 30 | 29,99 | 30,00 | 30,01 |

## Exercício 3 — Classificação Genérica

### Classes de equivalência do vento

| Classe | Velocidade | Classificação |
|---|---|---|
| 1 | v < 20 | Calmo |
| 2 | 20 ≤ v < 40 | Moderado |
| 3 | 40 ≤ v < 60 | Forte |
| 4 | v ≥ 60 | Tempestade |

### Valores-limite

| Fronteira | Abaixo | Na fronteira | Acima |
|---|---|---|---|
| 20 | 19,9 | 20 | 20,1 |
| 40 | 39,9 | 40 | 40,1 |
| 60 | 59,9 | 60 | 60,1 |

## Exercício 4 — Tabela de Decisão

O frete grátis é concedido somente quando:

- A: Valor da compra ≥ R$200.
- B: Cliente possui assinatura premium.
- C: Peso do pedido ≤ 30 kg.

### a) Tabela de decisão completa

S = Sim; N = Não.

| Regra | A | B | C | Frete grátis |
|---|---|---|---|---|
| R1 | S | S | S | S |
| R2 | S | S | N | N |
| R3 | S | N | S | N |
| R4 | S | N | N | N |
| R5 | N | S | S | N |
| R6 | N | S | N | N |
| R7 | N | N | S | N |
| R8 | N | N | N | N |

Foram implementados testes parametrizados para as oito regras.

### b) Tabela reduzida por Don't Care

O símbolo `-` representa uma condição irrelevante para a decisão.

| Regra | A | B | C | Frete grátis |
|---|---|---|---|---|
| T1 | S | S | S | S |
| T2 | N | - | - | N |
| T3 | S | N | - | N |
| T4 | S | S | N | N |

### Justificativas

**T1:** Todas as condições devem ser verdadeiras para conceder frete grátis.

**T2:** Se a compra for inferior a R$200, o frete será cobrado independentemente da assinatura premium e do peso. Abrange R5, R6, R7 e R8.

**T3:** Se a compra atingir R$200, mas o cliente não for premium, o peso não interfere na decisão. Abrange R3 e R4.

**T4:** Se o cliente for premium e a compra atingir R$200, mas o peso ultrapassar 30 kg, o frete será cobrado. Abrange R2.