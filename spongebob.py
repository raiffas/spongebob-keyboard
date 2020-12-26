from getkey import getkey, keys
from playsound import playsound

def main():
    while True:
        key = getkey()
        if key == keys.Q:
            playsound('resources/meanwhile_sound_effect.mp3')
        elif key == keys.W:
            playsound('resources/A_Few_Moments_Later_SpongeBob_Time_Card_8.mp3')
        elif key == keys.E:
            playsound('resources/Patrick_Booing_Sound_Effect__Download.mp3')
        elif key == keys.R:
            playsound('resources/SpongeBob_-_Squidward_youre_back_Sound_effect__Download.mp3')
        elif key == keys.T:
            playsound('resources/Spongebob_-_Alright_pinhead_Sound_Effect__Download.mp3')
        elif key == keys.Y:
            playsound('resources/Spongebob_-_Okay_Im_ready_Sound_Effect__Download.mp3')
        elif key == keys.U:
            playsound('resources/Spongebob_-_Overtime_Sound_effect__Download.mp3')
        elif key == keys.I:
            playsound('resources/Spongebob_-_Weird_Gibberish_Sound_Effect__Download.mp3')
        elif key == keys.O:
            playsound('resources/Squidward_-_I_have_no_talent_Sound_Effect__Download.mp3')
        elif key == keys.P:
            playsound('resources/Squidward_-_Shut_up_Slapping_Sound_Effect__Download.mp3')
        elif key == keys.ESC:
            return
        else:
            print("key not found")




main()
