#!/usr/bin/env python

import dbus
from gi.repository import GLib
import dbus.mainloop.glib

# Set your target window ID here (replace '0xXYZ' with your actual window ID)
TARGET_WINDOW_ID = '0x05800004'

def response_handler(response, result):
    if response == 0:
        print(f'Screenshot file: {result.get("uri")}')
    else:
        print("Failed to get screenshot")

def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    my_name = bus.get_connection().get_unique_name()[1:].replace(".", "_")
    response_path = f"/org/freedesktop/portal/desktop/request/{my_name}/my_token"
    bus.add_signal_receiver(
        response_handler,
        dbus_interface="org.freedesktop.portal.Request",
        path=response_path,
    )

    desktop = bus.get_object("org.freedesktop.portal.Desktop", "/org/freedesktop/portal/desktop")

    # Use `window` argument to specify the target window
    desktop.Screenshot("Screenshot", {"handle_token": "my_token", "window": TARGET_WINDOW_ID},
                       dbus_interface="org.freedesktop.portal.Screenshot")

    loop = GLib.MainLoop()
    loop.run()

if __name__ == "__main__":
    main()
