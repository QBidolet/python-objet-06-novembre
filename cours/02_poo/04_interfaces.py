from abc import ABC, abstractmethod


# Etape 1 : Créer notre interface.
class InterfacePaiement(ABC):
    @abstractmethod
    def effectuer_paiement(self, montant):
        """ Effectue les paiements dans un montant spécifié. """
        pass


# Etape 2 : Implementer différents types de paiements
class PaiementParCarte(InterfacePaiement):
    def effectuer_paiement(self, montant):
        print(f"Paiement de {montant} par carte.")


class PaiementParPaypal(InterfacePaiement):
    def effectuer_paiement(self, montant):
        print(f"Paiement de {montant} par Paypal.")
