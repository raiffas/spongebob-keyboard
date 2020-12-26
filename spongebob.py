from getkey import getkey, keys
from playsound import playsound

def main():
    while True:
        key = getkey()
        if key == keys.Q:
            playsound('resources/meanwhile_sound_effect.mp3')
            print(keys.Q)
        elif key == keys.W:
            print(keys.W)
        elif key == keys.E:
            print(keys.E)
        elif key == keys.R:
            print(keys.R)
        elif key == keys.T:
            print(keys.T)
        elif key == keys.Y:
            print(keys.Y)
        elif key == keys.U:
            print(keys.U)
        elif key == keys.I:
            print(keys.I)
        elif key == keys.O:
            print(keys.O)
        elif key == keys.P:
            print(keys.P)
        elif key == keys.ESC:
            return
        else:
            print("key not found")




main()
