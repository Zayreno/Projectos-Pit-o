from Equipa import Equipa


class Jogo:
    def __init__(self, equipaA: Equipa, equipaB: Equipa, golosA: int, golosB: int):
        self.equipaA = equipaA
        self.equipaB = equipaB
        self.golosA = golosA
        self.golosB = golosB

    def equipa_vencedora(self) -> Equipa | None:
        if self.golosA > self.golosB:
            return self.equipaA
        elif self.golosA < self.golosB:
            return self.equipaB
        return None
