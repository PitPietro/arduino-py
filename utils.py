def analog_state(analog_input):
    if analog_input.read():
        return 'UP'
    else:
        return 'DOWN'
