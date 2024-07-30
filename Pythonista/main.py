from abc import ABC, abstractmethod

class monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, nivel):
        pass

    def diminuir_claridade(self, nivel):
        pass


class monitor_full_hd(monitor):
    def aumentar_claridade(nivel):
        print(f"aumentado o brilho em {nivel}")

    def diminuir_claridade(nivel):
        print(f"diminuindo o brilho em {nivel}")

monitor_full_hd.aumentar_claridade(5)
monitor_full_hd.diminuir_claridade(6)