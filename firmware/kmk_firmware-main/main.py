import board
import busio
import displayio
import terminalio
import neopixel
import adafruit_imageload

from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation

displayio.release_displays()

# Layer Colors:
layer0 = (29, 45, 68)
layer1 = (62, 92, 118)
layer2 = (115, 140, 171)
layer3 = (255, 255, 255)
layer4 = (255, 255, 255)

# Layer Icons
ilayer0 = "/images/paste_inverse.bmp"
ilayer1 = "/images/folder.bmp"
ilayer2 = "/images/mic1.bmp"
ilayer3 = "/images/error.bmp"
ilayer4 = "/images/error.bmp"

# LEDs (SK6812)

led_num = 6 # Number of leds used
pixels = neopixel.NeoPixel(board.D6, led_num, auto_write = True)

# Turn off all Leds on boot
pixels.fill((0, 0, 0))



# OLED Setup
i2c = busio.I2C(scl = board.D5, sda = board.D4)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c) # Change if different adress

W = 128
H = 32

display = SSD1306(display_bus, width = W, height = H)

# Splash Group
splash = displayio.Group()
display.show(splash)

# Text Setup
text_area = label.Label(
    terminalio.FONT,
    text = "Test?",
    color = 0xFFFFFF,
    x = 0,
    y = H // 2
)

# Image Setup

# Example image
bitmap, palette = adafruit_imageload.load(
    "/images/paste_inverse.bmp",
    bitmap = displayio.Bitmap,
    palette = displayio.Palette
)

icon = displayio.TileGrid(
    bitmap,
    pixel_shader=palette,
    x=0,
    y=0
)

# Append Images
splash.append(text_area)
splash.append(icon)

# Keyboard Setup

keyboard = KMKKeyboard()

def before_matrix_scan(kbd):
    layer_update(kbd)

keyboard.before_matrix_scan = before_matrix_scan

#Indivdual GPIO for each key:
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3) # Each COLOMN individual gpio
keyboard.row_pins = (board.D7,) # The "row" gpio; uses a random free gpio
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Encoder Setup
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D8, board.D9, board.D10, False)
)

encoder_handler.map = [
    # Layer 0 - #-0-1
    [
        (KC.TO(1), KC.NO, KC.P) #REPLACE THE PUSH
    ],

    # Layer 1 - 0-1-2
    [
        (KC.TO(2), KC.TO(0), KC.P)
    ],
    
    # Layer 2 - 1-2-3
    [
        (KC.TO(3), KC.TO(1), KC.P)
    ],

    # Layer 3 - 2-3-4 (Layers after this are extra space for expansion for gaming, productivity, etc)
    [
        (KC.TO(4), KC.TO(2), KC.P)
    ],

    # Layer 4 - 3-4-#
    [
        (KC.NO, KC.TO(3), KC.P)
    ]
    
]


# Keymap
keyboard.keymap = [
    #layer 0
    [KC.COPY, KC.PASTE, KC.REDO, KC.UNDO],

    #layer 1 - (I already have a stero sound system so no need for volume wheel)
    [KC.LCTL(KC.F), KC.RWIN(KC.V), KC.RWIN(KC.E), KC.RWIN(KC.LSFT(KC.S))], #CTRL + F, clipboard, File explorer, Screenshots

    #layer 2
    [KC.MEDIA_PLAY_PAUSE, KC.LCTL(KC.LSFT(KC.M)), KC.LCTL(KC.LSFT(KC.B)), KC.MUTE], # Pause unpause, mute discord mic, defen discord, mute pc

    #ETC - MORE WHEN I FEEL LIKE IT :D

    #layer 3
    [KC.NO, KC.NO, KC.NO, KC.NO]

    #layer 4
    [KC.NO, KC.NO, KC.NO, KC.NO]

]


# Menu!

# Check what layer we are on:
def what_layer(keyboard):
    if not keyboard.active_layers:
        return 0
    return keyboard.active_layers[-1]

# Turn the layer led on and change the colors:
def layer_led(layer):
    pixels.fill((0, 0, 0))

    if layer == 0:
        pixels[0] = layer0
    
    elif layer == 1:
        pixels[0] = layer1
        pixels[1] = layer1

    elif layer == 2:
        pixels[0] = layer2
        pixels[1] = layer2
        pixels[2] = layer2
    
    elif layer == 3:
        pixels[0] = layer3
        pixels[1] = layer3
        pixels[2] = layer3
        pixels[3] = layer3
    
    else:
        pixels[0] = layer4
        pixels[1] = layer4
        pixels[2] = layer4
        pixels[3] = layer4
        pixels[4] = layer4

# Preload images
loaded_icons = {}
def preload_icon(filename):
    bitmap, palette = adafruit_imageload.load(
        filename,
        bitmap=displayio.Bitmap,
        palette=displayio.Palette
    )
    loaded_icons[filename] = (bitmap, palette)

# Preload images to Ram
preload_icon(ilayer0)
preload_icon(ilayer1)
preload_icon(ilayer2)
preload_icon(ilayer3)
preload_icon(ilayer4)

# Update Screen
def layer_screen(layer):
    if layer == 0:
        text_area.text = f"Copy\nPaste\nRedo\nUndo"
        set_icon(ilayer0, 99, 0)

    elif layer == 1:
        text_area.text = f"Find\nClip\nFiles\nShot"
        set_icon(ilayer1, 97, 1)
    
    elif layer == 2:
        text_area.text = f"Pause\n Mute\nDefen\n Mute PC"
        set_icon(ilayer2, 97, 0)

    elif layer == 3:
        text_area.text = f"Woah...\nNothing\nHere"
        set_icon(ilayer3, 1, 0)
    
    else:
        text_area.text = f"Woah...\nNothing\nHere"
        set_icon(ilayer4, 1, 0)

def set_icon(filename, x_cord, y_cord):
    bitmap, palette = loaded_icons[filename]
    new_icon = displayio.TileGrid(
        bitmap,
        pixel_shader=palette,
        x = x_cord,
        y = y_cord
    )

    splash[1] = new_icon

# Update everything
def layer_update(keyboard):
    global last_layer
    layer = what_layer(keyboard)
    if layer != last_layer:
        last_layer = layer
        layer_led(layer)
        layer_screen(layer)

last_layer = -1
layer_update(keyboard)

if __name__ == "__main__":
    keyboard.go()