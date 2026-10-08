from pathlib import Path
import datetime
 
 
#          caminho do módulo
#                  ^    
LOG_FILE = Path(__file__).parent / 'log.txt'
data_hour = datetime.datetime.now()
dt, hr = (data_hour.strftime("%Y-%m-%d"), data_hour.strftime("%H:%M:%S"))
 
 
 
class Log:  # Template method
 
    def _log(self, msg):  # Assinatura do método
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'error: {msg}')
 
    def log_success(self, msg):
        return self._log(f'success: {msg}')
    
 
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg}'  # {self.__class__.__name__}'
        with open(LOG_FILE, 'a') as file:
            file.write(f'{dt}, {hr}\n{msg_formatada}\n')
            file.write('\n')
            
    # @property
    # def log(self):
    #     return self._log
    
    # @log.setter
    # def log(self, log):
    #     self.log = log
 
 
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} | {self.__class__.__name__}')
        
        
        
if __name__ == '__main__':
    
    # lp = LogPrintMixin()
    # lp.log_error('Não foi possivel logar (lp)')
    # lp.log_success('Sucesso ao logar (lp)')
    
    lf = LogFileMixin()
    lf.log_error('Não foi possivel acessar (lf)')
    lf.log_success('Sucesso ao logar (lf)')