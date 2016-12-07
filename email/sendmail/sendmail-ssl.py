#coding:utf8
# apply to python 2.6.6 and python 2.7
#status: no ok

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

from_addr = 'fredmail03@126.com'
password = raw_input('Password: ')
to_addr = 'songjianhao@ucas.ac.cn'
to_addr1 = '280864129@qq.com'
smtp_server = 'smtp.126.com'
smtp_port = 587
with open('mail-text','r') as f:
    mail_text = f.read()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

msg = MIMEText(mail_text,'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr(u'管理员<%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候...', 'utf-8').encode()
print 'msg1=%s' % msg

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,[to_addr,to_addr1],msg.as_string())
server.quit()