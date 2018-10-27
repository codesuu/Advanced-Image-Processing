

def check(img, i, j, ie, je):
    BLACK = 0
    WHITE = 255
    for idx in range(i, ie):
        for jdx in range(j, je):
            if img[idx][jdx] == WHITE:
                return False
    return True


def erode(img):
    rows = img.shape[0]
    cols = img.shape[1]
    imgCp = img.copy()
    BLACK = 0
    WHITE = 255
    for col in range(cols):
        for row in range(rows):
            #  set row x col
            i = 0 if row - 2 < 0 else row - 2
            j = 0 if col - 2 < 0 else col - 2
            ie = rows if i + 3 >= rows else i + 3
            je = cols if j + 3 >= cols else j + 3
            imgCp[row][col] = BLACK if check(img, i, j, ie, je) else WHITE
    return imgCp


def dilate(img):
    rows = img.shape[0]
    cols = img.shape[1]

    imgCp = img.copy()
    BLACK = 0
    WHITE = 255
    for col in range(cols):
        for row in range(rows):
            if img[row][col] == BLACK:
                i = 0 if row - 2 < 0 else row - 2
                j = 0 if col - 2 < 0 else col - 2
                ie = rows if i + 3 >= rows else i + 3
                je = cols if j + 3 >= cols else j + 3
                for idx in range(i, ie):
                    for jdx in range(j, je):
                        imgCp[idx][jdx] = BLACK
    return imgCp


def opening(img):
    # after erode, dilate
    img = erode(img)
    img = dilate(img)
    return img


def closing(img):
    img = dilate(img)
    img = erode(img)
    return img
