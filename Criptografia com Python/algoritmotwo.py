def cifra_de_vigenere_criptografar(mensagem, chave):
    resultado = ""
    chave = chave.lower()
    indice_chave = 0
    
    for char in mensagem:
        if char.isalpha():
            deslocamento = ord(chave[indice_chave % len(chave)]) - ord('a')
            if char.islower():
                resultado += chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
            elif char.isupper():
                resultado += chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
            indice_chave += 1
        else:
            resultado += char
    return resultado

def cifra_de_vigenere_descriptografar(mensagem, chave):
    resultado = ""
    chave = chave.lower()
    indice_chave = 0
    
    for char in mensagem:
        if char.isalpha():
            deslocamento = ord(chave[indice_chave % len(chave)]) - ord('a')
            if char.islower():
                resultado += chr((ord(char) - ord('a') - deslocamento) % 26 + ord('a'))
            elif char.isupper():
                resultado += chr((ord(char) - ord('A') - deslocamento) % 26 + ord('A'))
            indice_chave += 1
        else:
            resultado += char
    return resultado
