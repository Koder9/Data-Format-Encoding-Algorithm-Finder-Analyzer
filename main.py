import re
import base64

def check_hex_dump(string):
    splitted = string.split(" ")

    if len(splitted[0]) == 8:
        pass
    else:
        return False

    try:
        if splitted[1].isdigit() == True or splitted[2].isdigit() == True:
            return True
        else:
            return False
    except Exception:
        return False

def check_Hex(string):
    try:
        string = string.replace(" ", "").replace("%", "").replace(",", "").replace("0x", "").replace(";","").replace(":", "").replace("\n", "").replace("0x,", "")
        n = int(string,16)
        return True
    except ValueError:
        return False

def check_charcode(string):
    seperators = " ,;:\n"
    for x in seperators:
        if x in string:
            break
        else:
            return False
    string = string.replace(" ", "").replace(",", "").replace(";", "").replace(":", "").replace("\n", "")
    for x in string:
        if x.isdigit() == True:
            return True
            
        else:
            return False

def check_decimal(string):
    string = string.replace(" ", "").replace(",", "").replace(";", "").replace(":", "").replace("\n", "")
    if string.isdecimal() == True:
        return True
    else:
        return False

def check_binary(string):
    string = string.replace(" ", "").replace(",", "").replace(";", "").replace(":", "").replace("\n", "")
    for x in string:
        if x == "1" or x == "0":
            continue
        else:
            return False
    return True

def check_octal(string):
    string = string.replace(" ", "").replace(",", "").replace(";", "").replace(":", "").replace("\n", "")
    for x in string:
        if x.isdigit() == True:
            if int(x) <= 7:
                continue
            else:
                return False
        else:
            return False
    return True

def check_base32(string):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890="
    for x in string:
        if x in chars:
            continue
        else:
            return False
    return True

def check_base45(string):
    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_.-"
    for c in string:
        if c not in valid_chars:
            return False
    return True

def check_base58(string):
    valid_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    for c in string:
        if c not in valid_chars:
            return False
    return True

def check_base62(string):
    valid_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for c in string:
        if c not in valid_chars:
            return False
    return True

def check_base64(string):
    try:
        base64.b64decode(string)
        return True
    except Exception:
        return False

def check_base85(string):
    try:
        base64.b85decode(string)
        return True
    except Exception:
        return False

def check_base(string):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for x in string:
        if x in chars:
            continue
        else:
            return False
    return True

def check_bcd(string):
    string = string.replace(" ", "").replace(",", "").replace(";", "").replace(":", "").replace("\n", "")
    for x in string:
        if x == "1" or x == "0":
            continue
        else:
            return False
    return True

def check_html_entity(string):
    if string.startswith("&") and string.endswith(";"):
        pass
    else:
        return False
    if ";&#x" in string:
        return True
    else:
        return False

def check_url_encode(string):
    if "%" in string:
        return True
    else:
        return False

def check_amf(string):
    if string.startswith("."):
        return True
    else:
        return False

def check_hex_content(string):
    if string.startswith("|") and string.endswith("|"):
        return True
    else:
        return False

def check_braille(string):
    if string.startswith("⠃") and string.endswith("⠃"):
        return True
    else:
        return False

print("""
This script will check if your string matchs with a specific encoding.

Hex dump
Hex
Charcode
Decimal
Binary
Octal
Base32
Base45
Base58
Base62
Base64
Base85
Base
BCD
HTML Entity
Url Encode
AMF
Hex Content
Braille
""")

def main():
    string = input("Enter string to find encoding: ")
    if check_hex_dump(string) == True:
        print("hex dump")
    if check_Hex(string) == True:
        print("Hex")
    if check_charcode(string) == True:
        print("charcode")
    if check_decimal(string) == True:
        print("decimal")
    if check_binary(string) == True:
        print("binary")
    if check_octal(string) == True:
        print("octal")
    if check_base32(string) == True:
        print("base32")
    if check_base45(string) == True:
        print("base45")
    if check_base58(string) == True:
        print("base58")
    if check_base62(string) == True:
        print("base62")
    if check_base64(string) == True:
        print("base64")
    if check_base85(string) == True:
        print("base85")
    if check_base(string) == True:
        print("base")
    if check_bcd(string) == True:
        print("bcd")
    if check_html_entity(string) == True:
        print("html entity")
    if check_url_encode(string) == True:
        print("url encode")
    if check_amf(string) == True:
        print("amf")
    if check_hex_content(string) == True:
        print("hex content")
    if check_braille(string) == True:
        print("braille")
    
if __name__ == "__main__":
    main()
