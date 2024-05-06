# for 循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则 python会难以追踪其中的元素
#要在遍历列表的同时修改，可以使用while循环

'''
    #7.3.1 在列表之间移动元素

    #首先创建一个待验证用户列表 和一个用于纯纯已验证用户的空列表
    unconfirmed_users = ['alice' ,' brain', 'candace']
    confirmed_users = []
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print("Verfing user:" + current_user.title())
        confirmed_users.append(current_user)
    print('\n following users have been confirmed')
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
'''

'''
    # 可以删除包含特定值的所有列表元素
    pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)
'''
# 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("what is your name? ")
    response = input(" which mountain would you like to clime? ")
    responses[name] = response
    repeat = input("would you like to let amother person respond ? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n---Poll results ")
for name,response in responses.items():
    print(name + "would like to climb" + response + ".")