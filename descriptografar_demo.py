from cryptography.fernet import Fernet #Importa a classe Fernet do pacote cryptography (submódulo fernet).
import os #Fernet implementa criptografia simétrica pronta para uso.

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):  # Cria um objeto de cifra/decifração a partir da chave fornecida
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome not in ["ransoware.py", "chave.key", "LEIA.txt"] and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
        print(f"Arquivo restaurado: {arquivo}")
    print("Todos os arquivos foram descriptografados com sucesso!")

if __name__ == "__main__":
    main()
