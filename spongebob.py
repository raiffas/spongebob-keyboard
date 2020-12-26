from getkey import getkey, keys


def main():
    while True:
        key = getkey()
        if key == keys.UP:
            print('up')
        elif key == keys.DOWN:
            print('down')
        elif key == keys.BANG:
            print(keys.BANG)
        elif key == keys.ESC:
            return
        else:
            print("key not found")




main()
