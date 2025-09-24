def on_button_pressed_a():
    global Pasos
    Pasos = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global Pasos
    music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    Pasos += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Pasos = 0
Pasos = 0

def on_forever():
    basic.show_number(Pasos)
basic.forever(on_forever)
