# 可以用while来进行条件判断 在python中 for循环与while循环的概念并不一致
# 前者更希望每一部分 后者是希望遇到条件就停止
'''
    prompt = " Tell me something, and I will repaet it back to you:"
    prompt += "Enter 'quit' to end the program"
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            antive = False
            # break 可以立刻退出循环 任何python循环中都可以使用break语句
        else:
            print(message)
'''

'''
    # 在循环中可以使用continue语句，可以根据条件测试结果决定是否继续执行循环 比如一个从1到10 但却只打印其中奇数的循环
    
    # 如果陷入无限循环 可以按Ctrl + C
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 ==0:
            continue
        print(current_number)
'''

pizza = 'Tell me what mix do you want '
pizza +=  "\n print quit to leave"
f = True
while f:
    message = input(pizza)

    if message == 'quit':
        f = False
    else:
        print('we have add this ' + message)