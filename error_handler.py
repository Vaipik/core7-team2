from errors import *


def error_handler(function):

    def wrapper(*args, **kwargs):

        try:
            return function(*args, ** kwargs)
        except KeyError as e:
            return str(e)
        except ValueError as e:
            return str(e)
        except IndexError:
            return 'Looks like you forgot to enter some data'
        except EmptySearchString as e:
            return str(e)
        except ContactExists as e:
            return str(e)
        except WrongBirthday as e:
            return str(e)
        except WrongEmail as e:
            return str(e)
        except WrongPhone as e:
            return str(e)

    return wrapper
