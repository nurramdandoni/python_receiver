import ctypes
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Map keys to virtual key codes
VK_CODE = {
    'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 'g': 0x47,
    'h': 0x48, 'i': 0x49, 'j': 0x4A, 'k': 0x4B, 'l': 0x4C, 'm': 0x4D, 'n': 0x4E,
    'o': 0x4F, 'p': 0x50, 'q': 0x51, 'r': 0x52, 's': 0x53, 't': 0x54, 'u': 0x55,
    'v': 0x56, 'w': 0x57, 'x': 0x58, 'y': 0x59, 'z': 0x5A,
    '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35,
    '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39,
    ' ': 0x20, '.': 0xBE, ',': 0xBC, ';': 0xBA, ':': 0xBA,
    '!': 0x31, '@': 0x32, '#': 0x33, '$': 0x34, '%': 0x35,
    '^': 0x36, '&': 0x37, '*': 0x38, '(': 0x39, ')': 0x30,
    '-': 0xBD, '_': 0xBD, '=': 0xBB, '+': 0xBB,
    '[': 0xDB, ']': 0xDD, '{': 0xDB, '}': 0xDD,
    '\\': 0xDC, '|': 0xDC, '\'': 0xDE, '"': 0xDE,
    '/': 0xBF, '?': 0xBF,'enter': 0x0D
}

SHIFT_KEYS = {
    '!': True, '@': True, '#': True, '$': True, '%': True,
    '^': True, '&': True, '*': True, '(': True, ')': True,
    '_': True, '+': True, '{': True, '}': True,
    '|': True, '"': True, '?': True,
    ':': True, '<': True, '>': True
}

def press_key(hexKeyCode, shift=False):
    if shift:
        ctypes.windll.user32.keybd_event(0x10, 0, 0, 0)  # Press Shift key
    ctypes.windll.user32.keybd_event(hexKeyCode, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(hexKeyCode, 0, 2, 0)
    if shift:
        ctypes.windll.user32.keybd_event(0x10, 0, 2, 0)  # Release Shift key

def send_keys(text):
    for char in text:
        if char == '\n':
            hexKeyCode = VK_CODE.get('enter')
            shift = False
        else:
            hexKeyCode = VK_CODE.get(char.lower())
            shift = SHIFT_KEYS.get(char, False)
        if hexKeyCode:
            press_key(hexKeyCode, shift)

@app.route('/scan_input', methods=['POST'])
def scan_input():
    data = request.get_json()
    text = data.get('text')

    if text is not None:
        send_keys(text)
        return jsonify({'message': 'Text input successfully!'}), 200
    else:
        return jsonify({'error': 'Invalid data!'}), 400
@app.route('/scan_input', methods=['GET'])
def scan_input_get():
    text = request.args.get('s')
    
    if text is not None:
        send_keys(text)
        return jsonify({'message': 'Text input successfully!'}), 200
    else:
        return jsonify({'error': 'Invalid data!'}), 400
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
