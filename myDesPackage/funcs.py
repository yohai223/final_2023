def check_bits(data: str):
    if len(data) == 7:
        return data
    if len(data) < 7:
        return "0" * (7 - len(data)) + data
    return ""


def text_to_binary(data: str):
    btext = bytes(data, 'utf-8')
    ret = ""
    for b in btext:
        add = "{0:b}".format(int(b))
        ret += check_bits(add)
    return ret


def binary_to_string(data: str):
    i = 0
    asc = []
    ret = ""
    while i < len(data) - 6:
        asc.append(int(data[i:i+7], base=2))
        i += 7
    for i in asc:
        #print(chr(int(i)))
        ret += str(i) #chr(i)
    return ret


def div_to_64(txt: str):
    chunks = [txt[i:i + 64] for i in range(0, len(txt), 64)]
    return chunks


def encrypt_text(text: str, key:str):
    chunks = div_to_64(text_to_binary(text))
    ret = ""
    for i in chunks:
        if len(i) == 64:
            ret += encrypt(i, key)
        else:
            ret += i
    return ret