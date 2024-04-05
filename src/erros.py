class Erro(Exception):
    def __init__(self, msg='') -> None:
        self.msg = msg
        super().__init__(msg)


class FalhaInterna(Erro):
    ...


class NaoEncontrado(Erro):
    ...


class Duplicado(Erro):
    ...
