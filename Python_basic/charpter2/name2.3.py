name = "ada lovelace"
#方法title()是可对数据执行的操作
# name 后面的 (.) 让Python对变量name执行方法title()指定的操作
# 每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成其工作

"""
    2.3.1
    title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
    upper()字符串全改为大写
    lower()字符串全改为小写
    存储数据时，很多情况下需要依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再去存储。
    
    2.3.2 合并（拼接）字符串
    很多情况下，需要合并字符串。比如可能想把姓和名存储在不同的变量中，等要显示姓名时再合而为一
    
    first_name = 'ada'
    last_name = 'lovelace'
    full_name = first_name + " " +last_name
    print(full_name)
    这种合并字符串的方法称为拼接。通过拼接，可以使用存储在变量中的信息来创建完整的信息。
    print("Hello" + full_name.title() + "!"
    
    2.3.3 使用制表符或换行符来添加空白
    在编程中，空白泛指任何非打印字符，如空格、制表符和换行符、
    在字符串中添加制表符，可使用字符组合\t
    print("\tpython")
    在字符串中添加换行符，可使用字符组合\n:
    print（“Language：\nPython\nC\nJaveScript")
    还可以同时包含制表符和换行符 "\n\t"
    print("Language:\n\tPython\n\tC\n\tJava“）
    
    2.3.4 删除空白
    空白很重要，经常需要比较两个字符串是否相等
    Python能够找出字符串开头和末尾多余的空白
    如果只删除 不赋回原值的话 那么删除就是暂时的
    strip()将字符串两端空白删除
    lstrip()将左端空白删除
    rstrip()将右端空白删除
    在实际程序中，这些剥除函数最常用于存储用户输入前对其进行清理
    
    2.3.5 使用字符串时避免语法错误
    例如，在用单括号括起的字符串中，如果包含撇号，就会导致错误、
    这是因为Python将第一个单括号和撇号之间的内容视为一个字符串，进而将余下的文本视为Python代码，从而引起错误。
"""
print(name.title())
print("Language:\n\tPython\n\tC\n\tJava")