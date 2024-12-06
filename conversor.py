# Função para converter Celsius para Fahrenheit
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32

# Função de conversão de Celsius para Kelvin
    def celsius_para_kelvin(celsius):
        return celsius + 273.15

# Função para converter Fahrenheit para Celsius
    def fahrenheit_para_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Função para converter Fahrenheit para Kelvin
    def fahrenheit_para_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

# Função para converter Kelvin para Celsius
    def kelvin_para_celsius(kelvin):
        return kelvin - 273.15

# Função para converter Kelvin para Fahrenheit
    def kelvin_para_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 +32

def exibir_menu():
    print("Bem vindo ao Conversor de temperaturas")
    print("Escolha a opção desejada:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Celsius")
    print("6 - Kelvin para Fahrenheit")
    print("7 - Sair")

def obter_entrada():
    try:
        temperatura = float(input("Digite o valor da temperatura: "))
        return temperatura
    except ValueError:
        print("Por favor, insira um número válido!")
        return obter_entrada()
    
def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-7): ")

        if escolha == '1':
            celsius = obter_entrada()
            resultado = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C = {resultado}°F")
        elif escolha == '2':
            celsius = obter_entrada()
            resultado = celsius_para_kelvin(celsius)
            print(f"{celsius}°C = {resultado}K")
        elif escolha == '3':
            fahrenheit = obter_entrada()
            resultado = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {resultado}°C")
        elif escolha == '4':
            fahrenheit = obter_entrada()
            resultado = fahrenheit_para_kelvin(fahrenheit)
            print(f"{fahrenheit}°F = {resultado}K")
        elif escolha == '5':
            kelvin = obter_entrada()
            resultado = kelvin_para_celsius(kelvin)
            print(f"{kelvin}K = {resultado}°C")
        elif escolha == '6':
            kelvin = obter_entrada()
            resultado = kelvin_para_fahrenheit(kelvin)
            print(f"{kelvin}K = {resultado}°F")
        elif escolha == '7':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__"