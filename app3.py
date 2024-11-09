
import threading

site = 'site'

def acessar_site(site):
    for i in range(20):
        print(f"acesssando site {i}/19")

def baixando_fotos():
    for i in range(20):
        print(f"baixando fotos {i}/19")


new_thread = threading.Thread(
    target=acessar_site, args=(site,), daemon=True)
new_thread.start()
baixando_fotos()
new_thread.join()
#