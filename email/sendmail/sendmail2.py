# -*- encoding: utf-8 -*-
# apply to python 2.6.6 and python 2.7

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

from_addr = 'fredmail03@126.com'
password = raw_input('Password: ') or 'sjh937841'
to_addr1 = 'songjianhao@ucas.ac.cn'
to_addr2 = 'fredmail16@sina.com'
smtp_server = 'smtp.126.com'
#with open('mail-text','r') as f:
#    mailtext = f.read()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr ))

msg = MIMEText('python student by LiaoXueFent', 'plain', 'utf-8',)
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr1)
msg['Subject'] = Header(u'来自SMTP的问候.....', 'utf-8').encode()
print "msg=%s" % msg
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(5)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addr1,to_addr2],msg.as_string())
server.quit()