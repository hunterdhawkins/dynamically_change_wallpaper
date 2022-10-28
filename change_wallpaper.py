'''
    Sources: https://stackoverflow.com/questions/32264960/how-to-use-change-desktop-wallpaper-using-python-in-ubuntu-14-04-with-unity
'''
import os
import random


def main():
    # Path to directory containing images
    dir_path = "/home/hunterhawkins/Desktop/wallpapers"
    # Get a list of the images
    list_of_images_in_dir = os.listdir(dir_path)
    random_image = random.choice(list_of_images_in_dir)
    # number_of_images = len(list_of_images_in_dir)

    set_image_string = "gsettings set org.gnome.desktop.background picture-uri-dark file://{dir}/{rand_img}".format(dir=dir_path, rand_img=random_image)
    # get_image_string = "gsettings get org.gnome.desktop.background picture-uri-dark"
    # print(get_image_string)
    os.system(set_image_string)


if __name__ == '__main__':
    main()