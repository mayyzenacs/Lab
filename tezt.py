from pytube import YouTube

def baixar_video(link):
    try:
        # Cria um objeto YouTube
        yt = YouTube(link)
        
        # Seleciona a melhor resolução disponível
        stream = yt.streams.get_highest_resolution()
        
        # Inicia o download
        print(f"Baixando '{yt.title}'...")
        stream.download()
        print("Download concluído!")
    except Exception as e:
        print("Ocorreu um erro:", e)

# Solicita o link do vídeo ao usuário
link = input("Digite o link do vídeo do YouTube: ")
baixar_video(link)
