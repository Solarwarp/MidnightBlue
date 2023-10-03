import bluetooth

def list_nearby_bluetooth_devices():
    print("Searching for Bluetooth devices...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_oui=True, device_id=-1, lookup_oui=True)
    print("Found {} devices.".format(len(nearby_devices)))

    print("Available Bluetooth devices:")
    print("Device Name\t\tMAC Address")
    print("-----------------------------------------")

    for addr, name, _ in nearby_devices:
        try:
            print(f"{name}\t\t{addr}")
        except UnicodeEncodeError:
            print(f"Unknown device\t\t{addr}")

if __name__ == "__main__":
    list_nearby_bluetooth_devices()
