import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
剩余时间生成
"""
def data_():
    timedata = '2025-04-20 08:00:00'
    future = datetime.datetime.strptime(timedata, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=8)
    # 当前时间
    now = datetime.datetime.now() + datetime.timedelta(hours=8)
    # 时间差
    delta = future - now
    hour = delta.seconds / 60 / 60
    minute = (delta.seconds - hour * 60 * 60) / 60
    seconds = delta.seconds - hour * 60 * 60 - minute * 60
    print_now = now.strftime('%Y-%m-%d %H:%M:%S')
    neirong = f"距离{future.year}年{future.month}月{future.day}日的专升本考试剩余：{delta.days}天"
    # print("\结余天数\":delta.days,hour,minute,seconds)
    return "现在是北京时间: "+print_now+"\n"+neirong

"""
邮件发送
"""
def sendMail(mail_subject, mail_content, recv_address):
    # param mail_content 邮件内容
    # param recv_address 接收邮箱
    sender_address = '1156415978@qq.com'
    sender_pass = 'mpmxzjuwhajtbagh'
    # 怎么申请应用密码可以往下看
    message = MIMEMultipart()  # message结构体初始化
    message['From'] = sender_address  # 你自己的邮箱
    message['To'] = recv_address  # 要发送邮件的邮箱
    message['Subject'] = mail_subject
    # mail_content,发送内容,这个内容可以自定义,'plain'表示文本格式
    message.attach(MIMEText(mail_content, 'plain'))
    # 这里是smtp网站的连接,可以通过谷歌邮箱查看,步骤请看下边
    session = smtplib.SMTP('smtp.qq.com', 587)
    # 连接tls
    session.starttls()
    # 登陆邮箱
    session.login(sender_address, sender_pass)
    # message结构体内容传递给text,变量名可以自定义
    text = message.as_string()
    # 主要功能,发送邮件
    session.sendmail(sender_address, recv_address, text)
    # 打印显示发送成功
    print("send {} successfully".format(recv_address))
    # 关闭连接
    session.quit()


if __name__ == '__main__':
    data = data_()
    sendMail("专升本倒计时", data, "2241007756@qq.com")
