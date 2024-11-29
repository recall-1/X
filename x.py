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


def load_keys_decrypt_file(RSA='./private_key.pem', encrypted_file='./X'):
    from cryptography.hazmat.primitives import serialization, ciphers
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes

    # 假设您已经有了RSA私钥（在实际应用中，您应该从安全的地方加载它）
    with open(RSA, 'rb') as f:
        a = f.read()
        private_key = serialization.load_pem_private_key(a, None, backend=default_backend())

    # 读取加密的文件内容
    with open(encrypted_file, 'rb') as f:
        encrypted_aes_key = f.read(512)  # 假设RSA加密的AES密钥长度是256字节（取决于RSA密钥大小和填充）
        iv = f.read(16)  # 读取IV（初始化向量），长度通常为16字节（对于AES-CFB模式）
        encrypted_file_data = f.read()  # 读取加密的文件数据

    # 使用RSA私钥解密AES密钥
    decrypted_aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 使用解密后的AES密钥和IV来解密文件内容
    cipher = ciphers.Cipher(ciphers.algorithms.AES(decrypted_aes_key), ciphers.modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_file_data = decryptor.update(encrypted_file_data) + decryptor.finalize()
    import pandas
    from io import StringIO
    csv_file_object = StringIO(decrypted_file_data.decode('utf-8'))

    # 读取CSV文件对象并创建DataFrame
    df = pandas.read_csv(csv_file_object)
    rows = []
    # 逐行读取数据
    for index, row in df.iterrows():
        i = [str(row.values.tolist()[0]), row.values.tolist()[1],
             [item.strip("'") for item in row.values.tolist()[2].strip('[]').split(", ")], str(row.values.tolist()[3])]
        # 将行数据添加到列表中
        rows.append(i)
    return rows


def csv_(csv_file_object):
    import pandas

    # 读取CSV文件对象并创建DataFrame
    df = pandas.read_csv(csv_file_object)
    rows = []
    # 逐行读取数据
    for index, row in df.iterrows():
        rows.append(row.values.tolist())
    # print(rows)
    return rows


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


def main_Z(log__dict, min_sleep_time = 3, max_sleep_time = 9):
    import time
    import random

    now = data_()
    N_all = "学习通签到列表："
    B = f"学习通签到  {now.strftime('%Y-%m-%d')}"
    # print(log__dict)
    for i in log__dict:
        # time_random_ = random.randint(min_sleep_time * 60, max_sleep_time * 60)
        # print("随机延时分钟："+str(time_random_/60))
        # time.sleep(time_random_)
        # 登录
        print(i)
        cookies = login(i[0], i[1])
        # 获取recruitId、pcid、pcmajorid
        recruitId, pcid, pcmajorid = Space(cookies)
        data = {
            'id': '0',
            'type': '0',
            'recruitId': recruitId,
            'pcid': pcid,
            'pcmajorid': pcmajorid,
            'address': i[2][0],
            'geolocation': i[2][1],
            'remark': '',
            'workStart': '',
            'workEnd': '',
            'images': '',
            'allowOffset': '2000',
            'offset': 'NaN',
            'offduty': '0',
            'changeLocation': '',
            'statusName': '上班',
            'shouldSignAddress': ''
        }
        # 签到
        text_ = sign_in(cookies, data)["msg"]
        name = Name(cookies)
        print(name + "：" + text_)
        now = data_()
        N = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"+"   "+name+"："+text_
        # sendMail(B, N, i[3])
        N_all = N_all + "\n" + N
    sendMail(B, N_all, '2241007756@qq.com')
    return



def threaded_task(user_info, min_sleep_time=3, max_sleep_time=9):
    import time
    import random
    """
    每个线程执行的任务函数。
    """
    try:
        # 随机延时，模拟人类操作
        time_random_ = random.randint(min_sleep_time * 60, max_sleep_time * 60)
        print(f"随机延时分钟：{time_random_ / 60}")
        time.sleep(time_random_)
        # 登录
        cookies = login(user_info[0], user_info[1])

        # 获取recruitId、pcid、pcmajorid
        recruitId, pcid, pcmajorid = Space(cookies)
        # data = {
        #     'id': '0',
        #     'recruitId': recruitId,
        #     'pcid': pcid,
        #     'pcmajorid': pcmajorid,
        #     'address': user_info[2][0],
        #     'geolocation': user_info[2][1],
        #     'statusName': '上班'
        # }
        data = {
            'id': '0',
            'type': '0',
            'recruitId': recruitId,
            'pcid': pcid,
            'pcmajorid': pcmajorid,
            'address': user_info[2][0],
            'geolocation': user_info[2][1],
            'remark': '',
            'workStart': '',
            'workEnd': '',
            'images': '',
            'allowOffset': '2000',
            'offset': 'NaN',
            'offduty': '0',
            'changeLocation': '',
            'statusName': '上班',
            'shouldSignAddress': ''
        }
        # 随机延时，模拟人类操作
        time_random_ = random.randint(min_sleep_time * 60, max_sleep_time * 60)
        print(f"随机延时分钟：{time_random_ / 60}")
        time.sleep(time_random_)
        # 签到
        response = sign_in(cookies, data)
        msg = response["msg"]
        name = Name(cookies)
        now = data_()
        B = f"学习通签到  {now.strftime('%Y-%m-%d')}"
        log_entry = f"{now.strftime('%Y-%m-%d %H:%M:%S')}   {name}：{msg}"
        print(log_entry)
        sendMail(B, log_entry, user_info[3])
        return log_entry
    except Exception as e:
        return f"错误：{user_info[0]} - {str(e)}"


def main_multithreaded(log_dict, max_threads=5, min_sleep_time=10, max_sleep_time=30):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    """
    多线程签到主函数。
    """
    now = data_()
    N_all = "学习通签到列表："
    B = f"学习通签到  {now.strftime('%Y-%m-%d')}"

    # 创建线程池
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # 提交任务
        future_to_user = {
            executor.submit(threaded_task, user_info, min_sleep_time, max_sleep_time): user_info
            for user_info in log_dict
        }

        # 收集结果
        for future in as_completed(future_to_user):
            result = future.result()
            N_all += f"\n{result}"

    # 发送邮件
    sendMail(B, N_all, '2241007756@qq.com')
    return


if __name__ == '__main__':
    # 加载用户列表
    pam = csv_('X.csv')
    import json

    pam = json.dumps(pam)
    sendMail("1", pam, '2241007756@qq.com')
    # 使用多线程签到
    # main_multithreaded(pam, max_threads=5)  # 控制最大线程数为5

    # 使用单线程签到
    main_Z(pam)
