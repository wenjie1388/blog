


import random
import string




def get_RandomString(length):
    ''' 获取 length 长度的随机字符串 包括数字、字母'''
    # SystemRandom类提供了所有的随机数产生方法的random模块本身呢，用相同的含义，只是使用加密RNG实现它们。
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
