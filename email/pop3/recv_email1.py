# -*- coding: utf-8 -*-

import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def guess_charset(msg):                                 #对msg检测编码
    charset = msg.get_charset()                         #获取msg的编码
    if charset is None:                                 #如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type','').lower()   #content_type  'text/html; charset="utf-8"'
        pos = content_type.find('charset=')             #从content_type对象中找到 'charset='字串的起始位置
        if pos >= 0:
            charset = content_type[pos + 8:].strip()        #如果charset=的起始位置大于0，  content_type[pos + 8:]表示从 charset= 之后开始取到最后，去除空格, charset= 正好是8个字符
    return charset                                         #返回编码

def decode_str(s):                                      #对输入的s进行解码
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    if indent == 0:                                     #如果indent == 0 从根容器提取From ,To, Subject的value
        for header in ['From', 'To', 'Subject']:      #从根容器遍历From ,To, Subject的value
            value = msg.get(header, '')
            if value:
                if header == 'Subject':                 # 如果value存在，且当前的header是Subject，对Subject的值解码
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)         # 如果value存在，但当前的header不是Subject(即From 或者 To 发件人或者收件人), 先解析地址: 如 管理员 <fredmail16@sina.com>
                    name = decode_str(hdr)               # 对名子进行解码, name 的值u'Python爱好者', 实际上是将base64编码转为unicode编码
                    value = u'%s <%s>' % (name, addr)   # addr = fredmail16@126.com
            print('%s%s: %s' % ('  ' * indent, header, value))      #打印缩进的空格， 邮件的From 或者To, 或者Subject, 以及相应的值

    if (msg.is_multipart()):                            #如果msg是multipart对象，即包含附件或者图片，就获取有效内容，枚举后再调用自身print_info()处理
        parts = msg.get_payload()                       #get_payload()返回list，包含所有的子对象:
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))     #打印缩进的空格
            print('%s----------------' % ('  ' * indent))
            print_info(part, indent + 1)                    #递归调用每一个子对象
    else:
        content_type = msg.get_content_type()           # 邮件对象不是一个MIMEMultipart,则获取msg的内容类型，就根据content_type判断:
        if content_type == 'text/plain' or content_type == 'text/html':     # 如果内容类型是纯文本或HTML:
            content = msg.get_payload(decode=True)              #就获取有效内容
            charset = guess_charset(msg)                        #检查msg的编码
            if charset:
                content = content.decode(charset)               #如果检测到msg编码，进行base64解码
            print('%sText: %s' % ('  ' * indent, content + '....'))     #打印缩进空格和邮件正文
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))    #打印缩进空格和附件和内容类型

email = 'fredmail16@sina.com'
password = raw_input('Password: ')
pop3_server = 'pop3.sina.com'

server = poplib.POP3(pop3_server)  #生成pop3对象，连接到POP3服务器
server.set_debuglevel(1)            # 可以打开或关闭调试信息:
print(server.getwelcome())          # 可选:打印POP3服务器的欢迎文字:

server.user(email)                  # 身份认证: 验证账号
server.pass_(password)              # 身份认证: 验证密码
print('Message: %s. Size: %s' % server.stat())          # stat()返回邮件数量和占用空间:
resp, mails, octets = server.list()                         # list()返回所有邮件的编号:
resp, lines, octets = server.retr(len(mails))               # lines存储了邮件的原始文本的每一行,
msg = Parser().parsestr('\r\n'.join(lines))                 # 可以获得整个邮件的原始文本:
print_info(msg)                                             # 稍后解析出邮件:
server.quit()                                               # 关闭连接

