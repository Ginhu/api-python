class Error(Exception):
    def __init__(self, msg='') -> None:
        self.msg = msg
        super().__init__(msg)
