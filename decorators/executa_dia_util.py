import datetime
import functools
import ctypes


def executar_dia_util(dia=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            hoje = datetime.datetime.now()
            if hoje.weekday() < 5 and hoje.day == dia:  
                return func(*args, **kwargs)
            else:
                ctypes.windll.user32.MessageBoxW(0, "bot não foi executado, hoje é fim de semana!!", "Aviso", 0x40)
                return None
        return wrapper
    return decorator
