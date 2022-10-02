import socket
'''with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        if interface is not None:
            sock.bind((interface, 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.connect((ip_address, port))
        for packet in packets
def create_magic_packet(F832E49A8814: str) -> bytes:
    
    Create a magic packet.

    A magic packet is a packet that can be used with the for wake on lan
    protocol to wake up a computer. The packet is constructed from the
    mac address given as a parameter.

    Args:
        macaddress: the mac address that should be parsed into a magic packet.

    
    if len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, "")
    elif len(macaddress) != 12:
        raise ValueError("Incorrect MAC address format")
        FFFFFFFFFFFF F832E49A8814
    return bytes.fromhex("F" * 12 + F832E49A8814 * 16'''
mac_address = input("input mac address: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.connect(("255.255.255.255", 9))
sock.send(bytes.fromhex("F" * 12 + f"{mac_address}" * 16))