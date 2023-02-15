from myTables import *


def xor(a: str, b: str):
    ret = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ret = ret + "0"
        else:
            ret = ret + "1"
    return ret


def shift_left(text: str, times: int):
    times = times % len(text)
    ret = text[times:] + text[:times]
    return ret


def bin2dec(binary: str):
    i = len(binary) - 1
    decimal = 0
    while i >= 0:
        if binary[i] == '1':
            decimal += 2**(len(binary) - i - 1)
        i -= 1
    return decimal


def permute(text: str, table):
    ret = [""] * len(table)
    for i in range(len(ret)):
        ret[i] = text[table[i] - 1]
    return "".join(ret)


def f(hb: str, sk: str):
    xored = xor(hb, sk)
    i = 0
    ret = ""
    for t in range(8):
        x = bin2dec(xored[i] + xored[i+5])
        y = bin2dec(xored[i+1:i + 5])
        val = sbox[t][x][y]
        ret += mp_int_to_bytes[str(val)]
        i += 6

    return ret


def key_switch(key: str):
    start = [3, 2, 1, 0]
    ret = ""
    for i in start:
        j = i
        while j < len(key):
            ret += key[j]
            j += 4
    return ret


def get_key_shifts(key: str):
    ret = []
    mid = int(len(key)/2)
    left = key[:mid]
    right = key[mid:]
    for i in shift_table:
        left = shift_left(left, i)
        right = shift_left(right, i)
        combine = left + right
        combine = permute(combine, key_comp)
        ret.append(combine)
    return ret


def encrypt(text: str, key: str, mode):
    text = hex_to_byte(text)
    key = hex_to_byte(key)
    key = permute(key, keyp)
    keys = get_key_shifts(key)
    if mode == "de":
        keys = keys[::-1]
    text = permute(text, initial_perm)
    mid = int(len(text) / 2)
    left, right = text[:mid], text[mid:]
    for i in range(16):
        rp = permute(right, exp_d)
        ans = f(rp, keys[i])
        ans = permute(ans, per)
        left = xor(left, ans)
        if i != 15:
            left, right = right, left
    ret = left + right
    ret = permute(ret, final_perm)
    return binary_to_hex(ret)


def hex_to_byte(text: str):
    ret = ""
    for c in text:
        ret += hex_to_binary_np[c]
    return ret


def binary_to_hex(data: str):
    ret = ""
    i = 0
    while i < len(data)-3:
        ret += binary_to_hex_mp[data[i:i+4]]
        i += 4
    return ret


def main():
    txt = "12ABBBBBCCCDDEE9"
    key = "AABB09182736CCDD"

    en = encrypt(txt, key, "en")
    print(en)
    print(encrypt(en, key, "de"))


if __name__ == '__main__':
    main()
