from functions import *
# префик по котором определяем нужные нам функции
FUN_PREFIX = 'fun_'

def get_fun_dict():
    """
    :return: словарь 'rule':function
    """
    rf = globals()
    rule_fun_dict = {}

    for fun in list(rf.items()):
        if fun[0].find(FUN_PREFIX) > -1:
            rule_name = fun[0][len(FUN_PREFIX):]
            rule_fun_dict[rule_name] = fun[1]

    return rule_fun_dict