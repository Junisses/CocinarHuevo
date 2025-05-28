import time

def countdown(segundos, callback_tick=None, callback_done=None):
    for s in range(segundos, -1, -1):
        if callback_tick:
            callback_tick(s)
        time.sleep(1)
    if callback_done:
        callback_done()