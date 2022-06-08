import os
import sys
import tty
import atexit
import termios

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setraw(sys.stdin)

sys.stdout.write("\033[?25l")
sys.stdout.flush()

@atexit.register
def restore_settings():
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

options = []
selected = 0

for path in os.listdir(os.path.abspath(os.curdir)):
    name = path.rsplit("/", 1)[-1]

    if os.path.isdir(path):
        name += "/"

    options.append({"name": name, "path": os.path.join(os.path.abspath(os.curdir), path), "sharing": False})

def clear():
    sys.stdout.write("\033[H\033[2J\033[3J")
    sys.stdout.flush()

def render_stepped():
    clear()

    print("\033[7m\033[1m[LEFT/RIGHT] Toggle sharing\033[0m", end="\r\n")
    print("\033[7m\033[1m[UP/DOWN] Select file/directory\033[0m", end="\r\n\n")

    for i, option in enumerate(options):
        if i == selected:
            sys.stdout.write("\033[1;32m")

        sys.stdout.write(option["name"])

        if i == selected or option["sharing"]:
            sharing = "sharing" if option["sharing"] else "not sharing"
            sys.stdout.write(f" | <{sharing}>")

        sys.stdout.write("\033[0m\r\n")

    sys.stdout.flush()

while True:
    render_stepped()
    ch = sys.stdin.read(1)
    ch_code = ord(ch)

    # Up arrow
    if ch_code == 65:
        selected = (selected - 1) % len(options)
        render_stepped()

    # Down arrow
    elif ch_code == 66:
        selected = (selected + 1) % len(options)
        render_stepped()

    # Right arrow
    elif ch_code == 67:
        options[selected]["sharing"] = not options[selected]["sharing"]
        render_stepped()

    # Left arrow
    elif ch_code == 68:
        options[selected]["sharing"] = not options[selected]["sharing"]
        render_stepped()
