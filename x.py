def data_():
    import datetime
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
    return print_now


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


def Q(cookies):
    import requests
    import json

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
    # cookies = {'SECKEY_ABVK': 'cSoDbLu2S9iuQ7rm9U1W6VVNmM7gBdpe8KyeUZq8kmQ%3D', 'BMAP_SECKEY': 'cSoDbLu2S9iuQ7rm9U1W6bwzdE-EaAQaRtnBmUCWX8sI6Uwnyzu9fLoww90MsdVVOIfSyoZ1bWY8T0Fjm9wdxz6Xwfq7m2_5gDLCZ-RJyFXsCV_5HBEuCMViSiHhtHq3F8K5C3uXQsP7XG3bAcVtjvRYM9IBNBUm8t85fKQPwXFbagdgYiCYPuqj4lmehmhd', 'lv': '1', 'fid': '319', '_uid': '249411517', 'UID': '249411517', 'vc': 'AC4DB98DF9BB70785D22E6183EF3DA13', 'xxtenc': '09d49d0689c6f44e67277874f7a93f58', 'fidsCount': '1', '_industry': '5', '_tid': '175669602', 'sso_puid': '249411517', 'wfwIncode': 'yqm319', 'wfwfid': '319', 'spaceFid': '319', 'source': 'num2', 'wfwEnc': 'D3FDDC278BBF9D4A974A857F67A156A8', 'route': '4b226ffea725727ea05ead170662c3b5', 'workUserId': '249411517', 'uf': '94ffe74515793f367fae9bc937961dcffb6346319506bdd698dc621e5ea63b2fa8689902fb364e86bf31460f022703bcc49d67c0c30ca5047c5a963e85f11099996c3ae7d7e1baf8fd68be96b6183b1af4751d19f3fc537a1d6f191b7e2de459b6476975eff8a7d8', '_d': '1732441344277', 'vc2': '285BBFAC033BED70E222936C191AA8FD', 'vc3': 'LjOfbbA1QAPUyVIpL88kSKMIkmIJLu%2FjpdLmiLA0n6HakNcbL3BW0KwrCQDZv9XOSY3%2Fh1wiQU1kk%2FFtA0AwRmDSNmfUHVFnv4sn870H9rjCO%2BrX84Wm4kqcxWK2%2FItG6BSZsYxuvXtHo1O8Z4eCMyJCJ9tyE0EiptvBMkfTzsY%3D51f8294ada17c00381098318d8f6a625', 'cx_p_token': '8b41749f233e82331bac663524ecba50', 'p_auth_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNDk0MTE1MTciLCJsb2dpblRpbWUiOjE3MzI0NDEzNDQyNzgsImV4cCI6MTczMzA0NjE0NH0.UNKGGtemC0YzxsCMR2NkokmUItnXmcLlG0u9KxnGIYs', 'DSSTASH_LOG': 'C_38-UN_5765-US_249411517-T_1732441344279', 'KI4SO_SERVER_EC': 'RERFSWdRQWdsckJiQXZ5ZmdkWW10bmVSV2NPYmJwa0U0bWpoU2JsaXFDNzlxZ2lkSEdkUVRCWmxO%0AVmQyVmxQTERtU2djWlRjU2NTVQp1NG13bWtscWxjQTRKdFN5MlYvcU5NaHNpdnlHWm9JN3dlclJt%0ARDFtdWE0OVd4bXBHSTZoTmxoY2k3cTRiL2Mvek9kZ3N5UTlGUEpZCnJUUXd6Mk14c3hMS2M0QWxj%0AaHYwWG9jL1QrcUl5UTlkOW5PLytCa0FMNXdmTWpUU1lpMFhsb1grbG16YjVGL1VKYS9IZldLLzlv%0AMkIKeW1ZVkZ3WjJuQ2FhbjRxelFlUENzakVOdzlNZDFFanVWb1JLY1pGeE1kYTdRVHdDRlVJQ2tw%0AUXdCZE16ZU9EVHh5RzBFVVp0c0tsQgozMG5kSUhFeDFydEJQQUlWclZTUHJRUzh6dk1DVHBib3FS%0AU2g3Yjl2N21TQWVjeUdlRjdNYXNOQUpHTkZpSlRSSEhucE5nSk9sdWlwCkZLSHRvaW5UTkEyMDQv%0AUVFVZEtLNnRwVkV5WXZkOVpBUUdSeWVPRFR4eUcwRVVhSkRtYzFabndpR1lOR0E5L2VLNmgzP2Fw%0AcElkPTEma2V5SWQ9MQ%3D%3D', 'INGRESSCOOKIE': '1732441353.553.22841.395124', 'JSESSIONID': 'DE58C774EAC316E929A5C552A817B643'}
    data = {
        'id': '0',
        'recruitId': '1959661',
        'pcid': '17279',
        'pcmajorid': '2515074',
        'address': '北京市昌平区科学园路18号博奥颐和健康科学技术(北京)有限公司',
        'geolocation': '116.282485,40.099942',
        'statusName': '上班',
    }

    html = requests.post(url, headers=headers, verify=False, cookies=cookies, data=data, proxies={'http':'120.220.220.95'})
    html.close()
    HTML_dict = json.loads(html.text)
    return HTML_dict


def login(username, passwd):  # 获取cookie
    import requests
    url = 'https://passport2-api.chaoxing.com/v11/loginregister'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
    data = {'uname': username, 'code': passwd, }
    session = requests.session()
    cookie_jar = session.post(url=url, data=data, headers=headers, proxies={'http':'120.220.220.95'}).cookies
    cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
    session.close()
    return cookie_t


def S(cookies):
    import requests
    import re

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
    html = requests.get(url, headers=headers, verify=False, cookies=cookies, proxies={'http': '160.191.41.251'})
    # 编写正则表达式的查找规则
    pattern = re.compile("""<div class="user-mes">.*?</div>""", re.S)
    re_list = pattern.findall(html.text)  # 以正则表达查找对应的字符串
    pattern = re.compile("""<h3>(.*?)</h3>""", re.S)
    re_list = pattern.findall(re_list[0])  # 以正则表达查找对应的字符串
    return re_list[0]


if __name__ == '__main__':
    cookies = login("15985480950", "Ly010427")
    text_ = Q(cookies)["msg"]
    print(text_)
    name = S(cookies)

    # 时间提示
    import datetime
    # 当前时间
    now = datetime.datetime.now() + datetime.timedelta()
    print_now = now.strftime('%Y-%m-%d %H:%M:%S')
    sendMail(f"学习通签到  {now.strftime('%Y-%m-%d')}", print_now+"   "+name+"："+text_, '2179854230@qq.com')
    sendMail(f"学习通签到  {now.strftime('%Y-%m-%d')}", print_now+"   "+name+"："+text_, '2241007756@qq.com')
