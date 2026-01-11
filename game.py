from pygame import *
import sounddevice as sd
import scipy.io.wavfile as wav

fs = 44100
recording = None
is_recording = False
voice_file = "voice_record.wav"
minus_track = "MinusDuHast.mp3"

init()
mixer.init()
mixer.music.set_volume(0.5)

window_size = 1200, 600
window = display.set_mode(window_size)
clock = time.Clock()

font.init()
font_big = font.SysFont("Arial", 32)

btn_rect = Rect(425, 250, 350, 80)
rect_color = "#FFFFFF"
btn_text = "Запис"

def start_voice_recording():
    global recording
    recording = sd.rec(int(fs * 15), samplerate=fs, channels=1, dtype="int16")


def stop_voice_recording():
    global recording
    sd.stop()
    if recording is not None:
        wav.write(voice_file, fs, recording)

def play_song_and_voice_together():
    mixer.music.load(minus_track)
    mixer.music.play()
    voice_sound = mixer.Sound(voice_file)
    voice_sound.play()


while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

        if e.type == MOUSEBUTTONDOWN:
            if btn_rect.collidepoint(e.pos):
                if not is_recording:
                    rect_color = "#FF0000"  
                    btn_text = "Зупинити та послухати"
                    is_recording = True

                    mixer.music.load(minus_track)
                    mixer.music.play()
                    start_voice_recording()
                else:
                    rect_color = "#FFFFFF"
                    btn_text = "Запис"
                    is_recording = False

                    stop_voice_recording()
                    play_song_and_voice_together()

    window.fill("grey")
    draw.rect(window, rect_color, btn_rect)
    text_surf = font_big.render(btn_text, True, "black")
    window.blit(text_surf, (btn_rect.x + 20, btn_rect.y + 25))

    display.update()
    clock.tick(30)