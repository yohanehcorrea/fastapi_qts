def classificar_nota(nota: float) -> str:
    if nota < 0 or nota > 10:
        return "nota invalida"
    if nota >= 7:
        return "aprovado"
    if nota >= 5:
        return "recuperacao"
    return "reprovado"


def calcular_desconto(valor: float, cliente_vip: bool) -> float:
    if valor < 0:
        return -1

    if cliente_vip:
        return valor * 0.20

    if valor >= 100:
        return valor * 0.10

    return 0