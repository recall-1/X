def data_():
    # 时间提示
    import datetime
    # 当前时间
    now = datetime.datetime.now() + datetime.timedelta(hours=8)
    print_now = now.strftime('%Y-%m-%d %H:%M:%S')
    return now


def sendMail(mail_subject, mail_content, recv_address):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
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


def sign_in(cookies, data):
    import json
    import requests
    from faker import Faker
    fake = Faker()

    url = 'https://xingtai.dgsx.chaoxing.com/mobile/clockin/addclockin2'
    headers = {
        'Host': 'xingtai.dgsx.chaoxing.com',
        'Connection': 'keep-alive',
        'Content-Length': '496',
        'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; LIO-AN000 Build/PQ3A.190605.10231804; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 com.chaoxing.mobile/ChaoXingStudy_3_4.7.4_android_phone_593_53 (@Kalimdor)_1b78501d174c4919b8626b2fa37a3671',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://xingtai.dgsx.chaoxing.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://xingtai.dgsx.chaoxing.com/mobile/clockin/show?pcid=17279',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    html = requests.post(url, headers=headers, verify=False, cookies=cookies, data=data, proxies={'http': f'{fake.ipv4_public(network=False, address_class=None)}'})
    html.close()
    HTML_dict = json.loads(html.text)
    return HTML_dict


def Space(cookies):
    import re
    import requests
    from faker import Faker
    fake = Faker()

    url = 'https://xingtai.dgsx.chaoxing.com/mobile/clockin/show'
    headers = {'Host': 'xingtai.dgsx.chaoxing.com', 'Proxy-Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
               'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
    # headers = {'Host': 'xingtai.dgsx.chaoxing.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 9; LIO-AN000 Build/PQ3A.190605.10231804; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 com.chaoxing.mobile/ChaoXingStudy_3_4.7.4_android_phone_593_53 (@Kalimdor)_1b78501d174c4919b8626b2fa37a3671', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'zh_CN', 'X-Requested-With': 'com.chaoxing.mobile', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'https://xingtai.dgsx.chaoxing.com/dgsx/mobile?fidEnc=de2311c4986ebe27&uid=201661129&mappId=4210933&mappIdEnc=6784b7aa290021631215542742424722&appId=845f6a7d4e1f452bab9d9d2d478de272&appKey=G5vFYYTj7l4O7M65&code=jW6dsRRb&state=319', 'Accept-Encoding': 'gzip, deflate'}
    data = {}
    html = requests.get(url, headers=headers, verify=False, cookies=cookies, proxies={'http': f'{fake.ipv4_public(network=False, address_class=None)}'})
    recruitId = re.compile("""<input.*?id="recruitId".*?value="(.*?)".*?>""", re.S).findall(html.text)  # 以正则表达查找对应的字符串
    pcid = re.compile("""<input.*?id="pcid".*?value="(.*?)".*?>""", re.S).findall(html.text)  # 以正则表达查找对应的字符串
    pcmajorid = re.compile("""<input.*?id="pcmajorid".*?value="(.*?)".*?>""", re.S).findall(html.text)  # 以正则表达查找对应的字符串
    return recruitId, pcid, pcmajorid


def login(username, passwd):  # 获取cookie
    import requests
    from faker import Faker
    fake = Faker()

    url = 'https://passport2-api.chaoxing.com/v11/loginregister'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
    data = {'uname': username, 'code': passwd, }
    session = requests.session()
    cookie_jar = session.post(url=url, data=data, headers=headers, proxies={'http': f'{fake.ipv4_public(network=False, address_class=None)}'}).cookies
    cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
    session.close()
    return cookie_t


def Name(cookies):
    import re
    import requests
    from faker import Faker
    fake = Faker()

    url = 'https://v1.chaoxing.com/manage'
    headers = {'Host': 'v1.chaoxing.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
               'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
               'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
               'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1',
               'Sec-Fetch-Dest': 'document', 'Referer': 'https://v8.chaoxing.com/',
               'Accept-Encoding': 'gzip, deflate, br, zstd',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

    data = {}
    html = requests.get(url, headers=headers, verify=False, cookies=cookies, proxies={'http': f'{fake.ipv4_public(network=False, address_class=None)}'})
    # 编写正则表达式的查找规则
    pattern = re.compile("""<div class="user-mes">.*?</div>""", re.S)
    re_list = pattern.findall(html.text)  # 以正则表达查找对应的字符串
    pattern = re.compile("""<h3>(.*?)</h3>""", re.S)
    re_list = pattern.findall(re_list[0])  # 以正则表达查找对应的字符串
    return re_list[0]


def main_Z(log__dict, min_sleep_time = 5, max_sleep_time = 10):
    import time
    import random

    now = data_()
    N_all = "学习通签到列表："
    B = f"学习通签到  {now.strftime('%Y-%m-%d')}"
    for _, i in log__dict.items():

        # time_random_ = random.randint(min_sleep_time * 60, max_sleep_time * 60)
        # print("随机延时分钟："+str(time_random_/60))
        # time.sleep(time_random_)

        # 登录
        cookies = login(i[0], i[1])
        # 获取recruitId、pcid、pcmajorid
        recruitId, pcid, pcmajorid = Space(cookies)
        data = {
            'id': '0',
            'recruitId': recruitId,
            'pcid': pcid,
            'pcmajorid': pcmajorid,
            'address': i[2][0],
            'geolocation': i[2][1],
            'statusName': '上班'
        }
        # 签到
        text_ = sign_in(cookies, data)["msg"]
        name = Name(cookies)
        print(name + "：" + text_)
        now = data_()
        N = f"{now.strftime('%Y-%m-%d %H:%M:%S')}\t"+name+"："+text_+"\t签到地点："+i[2][0]
        # sendMail(B, N, i[3])
        N_all = N_all + "\n" + N
    sendMail(B, N_all, '2241007756@qq.com')
    return


if __name__ == '__main__':
    L = ["15985480950", "Ly010427",
         ['北京市昌平区科学园路18号博奥颐和健康科学技术(北京)有限公司', '116.282485,40.099942'],
         '2179854230@qq.com']
    # C = ["18733938365", "6693844835c",
    #      ['天津市静海区金海道10号', '117.005296,38.944587'],
    #      '2966268079@qq.com']
    Y = ["13690941874", "yll875875.",
         ['广东省河源市龙川县老隆镇梅子坑', '115.28771,24.115273'],
         "2981832209@qq.com"]
    W = ["18830861190", "wzh861190",
         ['河北省邯郸市肥乡区元固乡三里堤村', '114.834199,36.547739'],
         "3445945379@qq.com"]
    M = ["13283480787", "13283480787xxt",
         ['太阳城文化路149号金辉国贸大厦', '119.610262,39.93803'],
         "1741202165@qq.com"]
    log__dict = {
        "L" : L,
        # "C" : C,
        "Y" : Y,
        "W" : W,
        "M" : M
    }

    main_Z(log__dict)
