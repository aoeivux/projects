import requests

if __name__ == '__main__':
    musicURL = f'http://music.163.com/song/media/outer/url?id=1493636838.mp3'
    response=requests.get(musicURL)
    f=open('f://music//成都（女声）-施雨凡.mp3','wb')
    f.write(response.content)
    f.close()