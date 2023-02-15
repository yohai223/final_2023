from PIL import Image

BORDER_SIZE = 1


def check_pixel(t):
    r, g, b, a = t
    avg = (r + g + b)/3
    return avg < 10


def paint(length, im: Image, xy):
    start = xy[0] + get_black_len(im, xy) - length
    xye = (start, xy[1])
    for i in range(length):
        im.putpixel(xy, (235, 51, 36, 255))
        im.putpixel(xye, (235, 51, 36, 255))
        xy = (xy[0] + 1, xy[1])
        xye = (xye[0] + 1, xye[1])


def get_black_len(im: Image, xy):
    count = 0
    while check_pixel(im.getpixel(xy)):
        count += 1
        xy = (xy[0] + 1, xy[1])
    return count


def mark_red(im, fp):
    h = im.height.real
    w = im.width.real
    first = size = 3
    for row in range(h):
        for line in range(w):
            pix = (line, row)
            if check_pixel(im.getpixel(pix)):
                length = 4
                if first > 0:
                    length = get_black_len(im, pix) - length
                    first -= 1
                elif pix[1] + size + 1 < h and not check_pixel(im.getpixel((pix[0], pix[1] + size + 1))):
                    length = get_black_len(im, pix) - length
                    size -= 1

                paint(length, im, pix)
                break

    im.save(fp)


def get_square_stat(im):
    h = im.height.real
    w = im.width.real
    x, y, hr, wr = 0, 0, 0, 0
    first, seq = True, False
    for row in range(h):
        for line in range(w):
            pix = (line, row)
            if check_pixel(im.getpixel(pix)):
                if first:
                    x, y = pix
                    wr = get_black_len(im, pix)
                    seq = True
                    first = False
                if seq:
                    hr += 1
                break
            if line == x:
                seq = False
    return x, y, hr, wr


def in_center(fp):
    im = Image.open(fp)
    w = im.width.real
    f_mid = int(w / 2)
    x, y, hr, wr = get_square_stat(im)
    s_mid = int(x + wr/2)
    return abs(f_mid - s_mid) < 4, f_mid - s_mid


def get_black_lines(im):
    lines = []
    h = im.height.real
    w = im.width.real
    x, y, hr, wr = 0, 0, 0, 0
    first, seq = True, False
    for row in range(h):
        line = 0
        while line < w:
            pix = (line, row)
            if check_pixel(im.getpixel(pix)):
                length = get_black_len(im, pix)
                lines.append((pix, length))
                line += length
            line += 1

    return lines


def combine(groups):
    arr = groups
    ret = []
    for i in arr:
        print(i)
    arr.sort(key=lambda x: x[0])
    if len(arr) > 1:
        diff = arr[0][0]-[1][0]




def divide_by_middle(lines):
    groups = []
    for l in lines:
        mid = l[0][0] + l[1] / 2
        for g in groups:
            if abs(g[0] - mid) < 4:
                g[1].append(l)
                g[0] = (g[0] * len(g[1]) + mid)/(len(g[1]) + 1)
                break
        else:
            groups.append([mid, [l]])
    combine(groups)
    return groups


def mark_groups(im, groups, fp):
    for g in groups:
        arr = g[1]
        arr.sort(key=lambda x: x[0][1])
        first = BORDER_SIZE
        i = 0
        arr_l = len(arr)
        for l in arr:
            length = BORDER_SIZE
            if first > 0:
                first -= 1
                length = l[1]
            elif i + BORDER_SIZE >= arr_l:
                length = length = l[1]
            paint(length, im, l[0])
            i += 1
    im.save(fp)


if __name__ == '__main__':
    file_path = r"C:\Users\yohai\PycharmProjects\final_project_2023\files\test6s.png"
    open_file = Image.open(file_path)
    gs = divide_by_middle(get_black_lines(open_file))
    print(len(gs))
    #mark_groups(open_file, gs, file_path)
