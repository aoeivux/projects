import ctypes


def set_img_as_wallpaper(filepath):
     #ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
     ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)


#http://api.easou.com/api/bookapp/searchdzh.m?word=%E9%81%93%E5%90%9B&page_id=1&count=20&cid=eef_&os=ios&appverion=1049
if __name__ == '__main__':
    set_img_as_wallpaper('~/Downloads/1.jpg')