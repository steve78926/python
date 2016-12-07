# -*- coding: utf8 -*-
# apply to python 2.6.6 and python 2.7

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'fredmail03@126.com'
password = raw_input('password: ') or 'xjsjikwi'
print 'password=%s' % password
to_addr = 'fredmail16@sina.com'
smtp_server = 'smtp.126.com'


msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……png-inline','utf-8').encode()

#add MIMEText:
msg.attach(MIMEText('<html><body><h1>HELLO</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))

#add png file
with open('boy.png', 'rb') as f:
    mime = MIMEBase('image', 'png',filename='boy.png')
    mime.add_header('Content-Disposition', 'attachment', filename='boy.png')
    mime.add_header('Content-ID', '0')
    mime.add_header('X-Attachment-ID','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr],msg.as_string())
server.quit()