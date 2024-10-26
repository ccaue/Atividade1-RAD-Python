# Calculadora imc
# Salva os resultados em um arquivo txt e um banco de dados sqlite

import sqlite3


def calcular_imc(peso, altura):  # Função para calcular o IMC.
    imc = peso / (altura ** 2)
    return imc


def categoria_imc(imc):  # Função para categorizar a situação do usuário.
    if imc < 25:
        return "Abaixo do peso"
    elif 25 <= imc < 30:
        return "Peso ideal"
    elif 30 <= imc < 35:
        return "Sobrepeso"
    else:
        return "Obesidade"


def salvar_txt(peso, altura, imc, categoria):  # Função para salvar os resultados num arquivo txt
    with open("DadosEX01.txt", "a") as arquivo:
        arquivo.write(f"Peso: {peso}, Altura: {altura}, IMC:{imc:.2f}, Categoria: {categoria}\n")


def salvar_bd(peso, altura, imc, categoria):  # Função para salvar os resultados num arquivo db
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS resultados_imc (peso REAL, altura REAL, imc REAL, categoria TEXT)")

    cursor.execute("INSERT INTO resultados_imc (peso, altura, imc, categoria) VALUES(?, ?, ?, ?)",
                   (peso, altura, imc, categoria))
    conn.commit()
    conn.close()


def main():
    try:
        peso = float(input("Digite seu peso (Kg): "))
        altura = float(input("Digite sua altura (M): "))
        imc = calcular_imc(peso, altura)
        categoria = categoria_imc(imc)

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Sua situação: {categoria}")

        salvar_txt(peso, altura, imc, categoria)
        salvar_bd(peso, altura, imc, categoria)

        print("Resultados salvos.")

    except ValueError:
        print("Valores inválidos. Por favor insira valores válidos para altura e peso.")


if __name__ == '__main__':
    main()
