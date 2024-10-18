import threading

site = 'site'

def entrando_site(site):
    for i in range(5):
        print(f'entrando no site {i}')

def extraindo_dados():


dados = ['celular','monitor', 'fone de ouvido', 'alto falante', 'computador']

threads = []
for t in threads:
    new_thread = threading.Thread(target=entrando_site, args=(site,), daemon=True)
