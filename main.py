from utils import print_binary_func
from utils import create_binary_adaptive_image




def main():

    for i in range(4):
        image_path = 'images/ym{}.jpg'.format(i)
        mask = create_binary_adaptive_image(image_path)
        print_binary_func(mask, ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00'])
        print('\n\n')



if __name__ == '__main__':
    main()