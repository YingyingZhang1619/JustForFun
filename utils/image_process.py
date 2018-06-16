import cv2


def create_binary_image(path, thresh=150, height=220):
    """
    :param path:        image full path
    :param thresh:      segmentation pixel value
    :param height:      height of resized image
    :return:            binary image
    """
    img = cv2.imread(path)
    raw_h, raw_w = img.shape[:2]
    scale = height / raw_h
    width = raw_w * scale
    size = (int(width), int(height))
    resize_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    gray_image = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, thresh, 255, cv2.THRESH_BINARY)
    return binary_image


def create_gray_image(path, width=170):
    """
    :param path:        image full path
    :param width:       width of resized image
    :return:            gray image
    """
    img = cv2.imread(path)
    raw_h, raw_w = img.shape[:2]
    scale = width / raw_w
    height = raw_h * scale
    size = (int(width), int(height))
    resize_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    gray_image = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
    return gray_image

def create_binary_adaptive_image(path, width=170):
    """
    :param path:        image full path
    :param method:      ADAPTIVE_THRESH_GAUSSIAN_C ADAPTIVE_THRESH_MEAN_C
    :param width:       width of resized image
    :return:            binary image
    """
    gray_image = create_gray_image(path, width)
    binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, 5)
    return binary_image
