# -*- coding: utf-8 -*-
# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

def get_event():
    with open('key.log') as file:
        event = file.read()
    return event

def event_to_key(event):
    keyIndex = event.index("char") + 7
    key = event[keyIndex]
    return key

def key_check():
    event = get_event()
    key = parse_event(event)
    return key


if __name__ == '__main__':
    key_check()
