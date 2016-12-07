#-*- coding:utf-8 -*-
# apply to python 2.6.6 and python 2.7

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr = 'fredmail03@126.com'
password = raw_input('Password: ')
to_addr = 'fredmail16@sina.com'
smtp_server = 'smtp.126.com'

with open('mail-text','r') as f:
    mailtext = f.read()

msg = MIMEText('<html><body><h1>Hello</h1>' + mailtext +
               '<p> send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候....','utf-8').encode()
print 'msg=%s' % msg

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
