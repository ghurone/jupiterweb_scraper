class Error(Exception):
    """
        base class error
    """
    pass


class GrupoDisciplinaError(Error):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)


class DisciplinaError(Error):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)


class JupiterWebMsgError(Error):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)
        
