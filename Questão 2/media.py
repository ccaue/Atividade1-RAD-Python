# Calculadora de média
import matplotlib.pyplot as plt


def calcular_media(av1, av2, av3):  # Função para calcular a média aritmética.
    media = (av1 + av2 + av3) / 3
    return media


def verificar_media(media):  # Função para verificar aprovação do aluno.
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"


def criar_grafico(av1, av2, av3, media):  # Função para criar o gráfico
    notas = [av1, av2, av3, media]
    labels = ['AV1', 'AV2', 'AV3', 'Média']
    cores = ['blue', 'blue', 'blue', 'red']

    plt.bar(labels, notas, color=cores)
    plt.ylim(0, 10)
    plt.title('Notas AV1, AV2, AV3 e Média')
    plt.ylabel("Notas")

    plt.show()


def main():
    try:
        av1 = float(input("Digite a primeira nota: "))
        av2 = float(input("Digite a segundanota: "))
        av3 = float(input("Digite a terceira nota: "))

        media = calcular_media(av1, av2, av3)
        situacao = verificar_media(media)

        print(f"Sua média é: {media:.2f}")
        print(f"Sua situação: {situacao}")

        criar_grafico(av1, av2, av3, media)

    except ValueError:
        print("Valores inválidos. Por favor insira valores válidos para as notas.")


if __name__ == '__main__':
    main()
