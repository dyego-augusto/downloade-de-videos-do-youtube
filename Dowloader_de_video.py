import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox
from pytube import YouTube

# Função para baixar o vídeo
def baixar_video():
    url = url_var.get()
    pasta_destino = pasta_var.get()

    if not url or not pasta_destino:
        messagebox.showwarning("Aviso", "Por favor, insira a URL e escolha a pasta de destino.")
        return

    try:
        # Cria um objeto YouTube com a URL do vídeo
        yt = YouTube(url)
        
        # Escolhe o stream de vídeo com a melhor resolução
        stream = yt.streams.get_highest_resolution()
        
        # Mostra informações do vídeo
        print(f'Baixando: {yt.title}')
        
        # Faz o download do vídeo para a pasta de destino
        stream.download(output_path=pasta_destino)
        
        # Nomeia o arquivo baixado
        arquivo_baixado = os.path.join(pasta_destino, stream.default_filename)
        novo_nome = os.path.join(pasta_destino, yt.title + ".mp4")
        os.rename(arquivo_baixado, novo_nome)
        
        messagebox.showinfo("Sucesso", f'Vídeo baixado e salvo como: {novo_nome}')
        
    except Exception as e:
        messagebox.showerror("Erro", f'Ocorreu um erro: {e}')

# Função para selecionar a pasta de destino
def selecionar_pasta():
    pasta = filedialog.askdirectory()
    pasta_var.set(pasta)

# Criando a janela principal
janela = Tk()
janela.title("Downloader de Vídeos do youtube")

# Variáveis para armazenar os dados da interface
url_var = StringVar()
pasta_var = StringVar()

# Rótulos e campos de entrada
Label(janela, text="URL do Vídeo:").grid(row=0, column=0, padx=10, pady=10)
Entry(janela, textvariable=url_var, width=50).grid(row=0, column=1, padx=10, pady=10)

Label(janela, text="Pasta de Destino:").grid(row=1, column=0, padx=10, pady=10)
Entry(janela, textvariable=pasta_var, width=50).grid(row=1, column=1, padx=10, pady=10)

# Botão para escolher pasta
Button(janela, text="Selecionar Pasta", command=selecionar_pasta).grid(row=1, column=2, padx=10, pady=10)

# Botão para iniciar o download
Button(janela, text="Baixar Vídeo", command=baixar_video).grid(row=2, column=1, pady=20)

# Iniciar a janela
janela.mainloop()
