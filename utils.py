import numpy as np


def get_array(text: str):
    ret = []
    for i in text:
        ret.append(ord(i))
    return ret


def get_nums(letter: str):
    if len(letter) == 1:
        return 0, 0, int(letter)
    elif len(letter) == 2:
        return 0, int(letter[0]), int(letter[1])
    else:
        return int(letter[0]), int(letter[1]), int(letter[2])


def encript(im, ar, shape):
    for i in range(shape[0]):
        for j in range(shape[1]):
            coord = i * shape[1] + j
            if coord > len(ar)-1:
                return im
            letter = get_nums(str(ar[coord]))
            can = True
            for k in range(3):
                if im[i, j, k]+letter[k] >= 255:
                    can = False
            if can:
                im[i, j, 0] = im[i, j, 0]+letter[0]
                im[i, j, 1] = im[i, j, 1] + letter[1]
                im[i, j, 2] = im[i, j, 2] + letter[2]




if __name__ == '__main__':
    print(get_nums('23'))