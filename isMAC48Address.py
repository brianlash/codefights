# A media access control address (MAC address) is a unique identifier assigned
# to network interfaces for communications on the physical network segment.
#
# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly
# form is six groups of two hexadecimal digits (0 to 9 or A to F),
# separated by hyphens (e.g. 01-23-45-67-89-AB).
#
# Your task is to check by given string inputString whether it
# corresponds to MAC-48 address or not.


def isMAC48Address(inputString):

    valid = 'ABCDEF0123456789'

    mac_check = list(inputString)

    for i, x in enumerate(mac_check):
        if (i+1) % 3 == 0:
            if x != '-' or i == len(mac_check)-1 or i == len(mac_check) - 2:
                return False
        else:
            if x in valid:
                pass
            else:
                return False

    return True
