import serial.tools.list_ports


def assign_port():
    print("Scanning COM Ports...")

    selected_port = None

    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "USB Serial Port" in port.description and port.manufacturer == "FTDI":
            selected_port = port.device
            print(f"Port Scan Complete. Using Port {selected_port}")
            return selected_port

    return None