import threading

site = 'site'
dados = ['celular','monitor', 'fone de ouvido', 'alto falante', 'computador']


def entrando_site(site):
    for i in range(5):
        print(f'entrando no site {i}')

def extraindo_dados():
    for item in dados:
        print(item)



threads = []
for t in dados:
    new_thread = threading.Thread(target=entrando_site, args=(site,), daemon=True)
new_thread.start()
extraindo_dados()
new_thread.join()

