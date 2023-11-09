class MaClasse:
    def __init__(self):
        self.attribut_public = ("Je suis un attribut public, "
                                "accessible de partout.")
        self._attribut_protege = ("Je suis protégé, accessible"
                                 "uniquement depuis la classe"
                                 "et ses sous classes.")
        self.__attribut_prive = "Je suis un attribut privé."
