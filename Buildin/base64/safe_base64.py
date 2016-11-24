import base64

def safe_base64(s):

    mod = len(s)%4
    if mod == 0:
        news = s
    else:
        news = s + '='*mod
        print 'news: %s' % news
    return base64.b64decode(news)

if __name__ == '__main__':
    print safe_base64('YWJjZA=')

