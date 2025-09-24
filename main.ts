input.onButtonPressed(Button.A, function () {
    Pasos = 0
})
input.onGesture(Gesture.Shake, function () {
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    Pasos += 1
})
let Pasos = 0
Pasos = 0
basic.forever(function () {
    basic.showNumber(Pasos)
})
