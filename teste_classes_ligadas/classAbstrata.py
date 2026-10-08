from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        raise NotImplementedError('implemente o metodo log')
    def log_error(self, msg):
        return self._log(f'error: {msg}')
    def log_success(self, msg):
        return self._log(f'sucess: {msg}')

class LogPritnMixin(Log):
    def _log(self, msg):
        print(f'{msg}({self.__class__.__name__})')


l = LogPritnMixin()
l.log_error('oi')