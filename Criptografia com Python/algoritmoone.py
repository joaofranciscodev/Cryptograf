def main_menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Criptografar Mensagem")
        print("2. Descriptografar Mensagem")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            criptografar_menu()
        elif opcao == "2":
            descriptografar_menu()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def criptografar_menu():
    print("\n=== Criptografar Mensagem ===")
    print("1. Cifra de César")
    print("2. Segundo Algoritmo")
    
    algoritmo = input("Escolha um algoritmo: ")
    
    if algoritmo == "1":
        mensagem = input("Digite a mensagem para criptografar: ")
        chave = int(input("Digite a chave (número de posições para deslocar): "))
        mensagem_criptografada = cifra_de_cesar_criptografar(mensagem, chave)
        print("Mensagem Criptografada:", mensagem_criptografada)
    elif algoritmo == "2":
        # Implementação do segundo algoritmo
        pass
    else:
        print("Opção inválida. Tente novamente.")

def descriptografar_menu():
    print("\n=== Descriptografar Mensagem ===")
    print("1. Cifra de César")
    print("2. Segundo Algoritmo")
    
    algoritmo = input("Escolha um algoritmo: ")
    
    if algoritmo == "1":
        mensagem = input("Digite a mensagem para descriptografar: ")
        chave = int(input("Digite a chave (número de posições para deslocar): "))
        mensagem_descriptografada = cifra_de_cesar_descriptografar(mensagem, chave)
        print("Mensagem Descriptografada:", mensagem_descriptografada)
    elif algoritmo == "2":
        # Implementação do segundo algoritmo
        pass
    else:
        print("Opção inválida. Tente novamente.")

# Funções para a Cifra de César
def cifra_de_cesar_criptografar(mensagem, chave):
    resultado = ""
    for char in mensagem:
        if char.isalpha():
            deslocamento = chave % 26
            if char.islower():
                resultado += chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
            elif char.isupper():
                resultado += chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
        else:
            resultado += char
    return resultado

def cifra_de_cesar_descriptografar(mensagem, chave):
    return cifra_de_cesar_criptografar(mensagem, -chave)

# Programa principal
main_menu()
