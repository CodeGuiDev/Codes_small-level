class Meuerror(Exception):
    ...

def levantar():
    exception_ = Meuerror('a', 'b', 'c')
    exception_.add_note('olha minha primeira notinha rapaz')
    raise exception_
class Outroerror(Exception):
    ...

try:
    levantar()
except (Meuerror, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = Outroerror('vou lançar de novo') 
    raise exception_
