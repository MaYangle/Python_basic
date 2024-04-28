import math

import torch

message = "Hello python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)
# 在程序中可随时修改变量的值，而Python将始终记录变量的最新值
"""
    2.1
    变量名只能包含字母、数字和下划线，变量名可以字母或下划线打头，但不能以数字打头。
    例如 可以将变量命名为message_1,但不能将其命名为1_message
    
    变量名不能包含空格，但可以使用下划线来分隔其中的单词
    
    不要讲Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词。
    
    变量名应既简短又具有描述性 尽量描述干净而且还简短。
    
    慎用小写字母i 和大写字母O 因为它们可能被人错看成数字1和0  

"""

"""
    2.3 -字符串
    在Python中，可以用引号括起字符串，可以是单引号 也可以是多引号 这种灵活性很好
    
"""

def attention(query,key,value,mask=None,dropout=None):
    d_k  = query.size(-1)
    scores = torch.matmul(query,key.transponse(-2,-1)) / math.sqrt(d_K)
    weights = F.softmax(scores,dim=-1)
    return torch.matmul(weights,value),weights

