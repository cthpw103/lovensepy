from bluetooth.ble import *
def shutdown():
        services = "0000fff0-0000-1000-8000-00805f9b34fb", "6e400001-b5a3-f393-e0a9-e50e24dcca9e" # first and second gen toys
        haha = find_service(uuid = services)
# todo: add more
