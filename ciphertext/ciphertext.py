def creat_pw():
    import msvcrt
    print('请输入密码: ')
    li = []
    while 1:
        ch = msvcrt.getch()
    # 回车
        if ch == b'\r':
            msvcrt.putch(b'\n')
            return str(b''.join(li).decode())
    # 退格
        elif ch == b'\b':
            if li:
                li.pop()
                msvcrt.putch(b'\b')
                msvcrt.putch(b' ')
                msvcrt.putch(b'\b')
    # Esc
        elif ch == b'\x1b':
            break
        else:
            li.append(ch)
            msvcrt.putch(b'?')