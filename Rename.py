
import os

def renomear_arquivos(diretorio, prefixo):
    # Verifica se o diretório existe
    if not os.path.isdir(diretorio):
        print(f'O diretório "{diretorio}" não existe.')
        return
    
    # Obtém a lista de arquivos no diretório
    arquivos = os.listdir(diretorio)
    
    # Ordena os arquivos alfabeticamente
    arquivos_ordenados = sorted(arquivos)
    
    # Itera sobre cada arquivo e renomeia
    for idx, arquivo in enumerate(arquivos_ordenados):
        # Obtém o caminho completo do arquivo
        caminho_antigo = os.path.join(diretorio, arquivo)
        
        # Separa o nome do arquivo da sua extensão
        nome, extensao = os.path.splitext(arquivo)
        
        # Define o novo nome com o prefixo e a ordem
        novo_nome = f"{prefixo}_{idx + 1}{extensao}"
        
        # Obtém o caminho completo do novo arquivo
        caminho_novo = os.path.join(diretorio, novo_nome)
        
        # Renomeia o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f'Arquivo renomeado: "{arquivo}" para "{novo_nome}"')

# Diretório onde os arquivos estão localizados
diretorio_alvo = 'C:\Fellipe'

# Prefixo a ser adicionado aos nomes dos arquivos
prefixo = 'novo'

# Chama a função para renomear os arquivos
renomear_arquivos(diretorio_alvo, prefixo)
