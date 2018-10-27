import numpy as np


def binirize(img, th):
    final_img = img.copy()
    rows = img.shape[0]
    cols = img.shape[1]
    for i in range(rows):
        for j in range(cols):
            if final_img[i][j] > th:
                final_img[i][j] = 255
            else:
                final_img[i][j] = 0
    return final_img


def threshold_otsu(img):
    import numpy as np
    pixel_number = img.shape[0] * img.shape[1]
    mean_weigth = 1.0/pixel_number
    his, bins = np.histogram(img, np.arange(0, 257))
    final_thresh = -1
    final_value = -1
    intensity_arr = np.arange(256)
    for t in bins[1:-1]:
        pcb = np.sum(his[:t])
        pcf = np.sum(his[t:])
        Wb = pcb * mean_weigth
        Wf = pcf * mean_weigth

        mub = np.sum(intensity_arr[:t]*his[:t]) / float(pcb)
        muf = np.sum(intensity_arr[t:]*his[t:]) / float(pcf)
        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value
    return final_thresh


def threshold_optimal(img):
    pixel_number = img.shape[0] * img.shape[1]
    mean_weigth = 1.0/pixel_number
    his, bins = np.histogram(img, np.arange(0, 257))
    final_thresh = -1
    final_value = -1
    intensity_arr = np.arange(256)
    for t in bins[1:-1]:
        pcb = np.sum(his[:t])
        pcf = np.sum(his[t:])
        Wb = pcb * mean_weigth
        Wf = pcf * mean_weigth

        mub = np.sum(intensity_arr[:t]*his[:t]) / float(pcb)
        muf = np.sum(intensity_arr[t:]*his[t:]) / float(pcf)
        value = (Wb * Wf) / 2

        if value > final_value:
            final_thresh = t
            final_value = value
    return final_thresh
