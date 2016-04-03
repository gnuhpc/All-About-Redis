#11.1.5.1	 事件通知
在sentinel中，如果出现warning以上级别的事件发生， 是可以通过如下配置进行脚本调用的（对于该脚本redis启动用户需要有执行权限）：
	
	sentinel notification-script mymaster /redis/script/notify.py
比如说，我们希望在发生这些事件的时候进行邮件通知，那么，notify.py就是一个触发邮件调用的东东，传入第一个参数为事件类型，第二个参数为事件信息：

	#!/bin/python
	
	from sendmail import send_mail
	import sys
	
	event_type = sys.argv[1]
	event_desc = sys.argv[2]
	mail_content = event_type + ":" + event_desc
	
	send_mail("xxxx@qq.com",
	          ["xxxxx@cmbc.com.cn","xxxx@gmail.com"],
	          "Redis Sentinel Event Notification Mail",
	          mail_content,
	          cc=["xxx@gmail.com","xxx@139.com"],
	          bcc=["xxxx@qq.com"]
	        )

有两个注意事项：
1）	这个时候如果集群发生了切换会产生很多事件，此脚本是在每一个事件发生时调用一次，那么你将短时间收到很多封邮件，加上很多的邮件网关是不允许在一个短时间内发送太多的邮件的，因此这个仅仅是一个示例，并不具备实际上的作用。
2）	一般我们会采用多个sentinel，只需在一个sentinel上配置即可，否则将同一个消息会被多个sentinel多次处理。

附sendmail模块代码：
	
	import smtplib
	import os
	from email.mime.multipart import MIMEMultipart
	from email.mime.application import MIMEApplication
	from email.mime.base import MIMEBase
	from email.mime.text import MIMEText
	from email.utils import formatdate
	from email import Encoders
	from email.message import Message
	import datetime
	
	def send_mail(fromPerson,toPerson, subject="", text="",files=[], cc=[], bcc=[]):
	    server = "smtp.qq.com"
	    assert type(toPerson)==list
	    assert type(files)==list
	    assert type(cc)==list
	    assert type(bcc)==list
	
	    message = MIMEMultipart()
	    message['From'] = fromPerson
	    message['To'] = ', '.join(toPerson)
	    message['Date'] = formatdate(localtime=True)
	    message['Subject'] = subject
	    message['Cc'] = ','.join(cc)
	    message['Bcc'] = ','.join(bcc)
	    message.attach(MIMEText(text))
	
	    for f in files:
	        part = MIMEApplication(open(f,"rb").read())
	        part.add_header('Content-Disposition', 'attachment', filename=filename)
	        message.attach(part)
	
	    addresses = []
	    for x in toPerson:
	        addresses.append(x)
	    for x in cc:
	        addresses.append(x)
	    for x in bcc:
	        addresses.append(x)
	
	    smtp = smtplib.SMTP_SSL(server)
	    smtp.login("xxxx@qq.com","xxxx")
	    smtp.sendmail(message['From'],addresses,message.as_string())
	    smtp.close()

最佳实践：采用ELK（Elastic+Logstash+Kibana）进行日志收集告警（ElastAlert用起来不错），不启用这个事件通知功能。如果你的环境中没有ELK，或者启动一个Tcp Server进程，notify脚本将事件通过tcp方式吐给这个server，该Server收集一批事件后再做诸如发邮件的处理。
