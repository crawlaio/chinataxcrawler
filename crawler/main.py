# -*- coding: utf-8 -*-
import base64
import json
import time

import execjs
import requests
import urllib3

from predictCaptcha.picProcess import get_aim_letters

urllib3.disable_warnings()

citys = [
    {
        "code": "1100",
        "sfmc": "北京",
        "Ip": "https://fpcy.beijing.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.beijing.chinatax.gov.cn:443",
    },
    {
        "code": "1200",
        "sfmc": "天津",
        "Ip": "https://fpcy.tjsat.gov.cn:443/NWebQuery",
        "address": "https://fpcy.tjsat.gov.cn:443",
    },
    {
        "code": "1300",
        "sfmc": "河北",
        "Ip": "https://fpcy.hebei.chinatax.gov.cn/NWebQuery",
        "address": "https://fpcy.hebei.chinatax.gov.cn",
    },
    {
        "code": "1400",
        "sfmc": "山西",
        "Ip": "https://fpcy.shanxi.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.shanxi.chinatax.gov.cn:443",
    },
    {
        "code": "1500",
        "sfmc": "内蒙古",
        "Ip": "https://fpcy.neimenggu.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.neimenggu.chinatax.gov.cn:443",
    },
    {
        "code": "2100",
        "sfmc": "辽宁",
        "Ip": "https://fpcy.liaoning.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.liaoning.chinatax.gov.cn:443",
    },
    {
        "code": "2102",
        "sfmc": "大连",
        "Ip": "https://sbf.dalian.chinatax.gov.cn:8402/NWebQuery",
        "address": "https://sbf.dalian.chinatax.gov.cn:8402",
    },
    {
        "code": "2200",
        "sfmc": "吉林",
        "Ip": "https://fpcy.jilin.chinatax.gov.cn:4432/NWebQuery",
        "address": "https://fpcy.jilin.chinatax.gov.cn:4432",
    },
    {
        "code": "2300",
        "sfmc": "黑龙江",
        "Ip": "https://fpcy.hl-n-tax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.hl-n-tax.gov.cn:443",
    },
    {
        "code": "3100",
        "sfmc": "上海",
        "Ip": "https://fpcy.shanghai.chinatax.gov.cn:1001/NWebQuery",
        "address": "https://fpcy.shanghai.chinatax.gov.cn:1001",
    },
    {
        "code": "3200",
        "sfmc": "江苏",
        "Ip": "https://fpcy.jiangsu.chinatax.gov.cn:80/NWebQuery",
        "address": "https://fpcy.jiangsu.chinatax.gov.cn:80",
    },
    {
        "code": "3300",
        "sfmc": "浙江",
        "Ip": "https://fpcy.zhejiang.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.zhejiang.chinatax.gov.cn:443",
    },
    {
        "code": "3302",
        "sfmc": "宁波",
        "Ip": "https://fpcy.ningbo.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.ningbo.chinatax.gov.cn:443",
    },
    {
        "code": "3400",
        "sfmc": "安徽",
        "Ip": "https://fpcy.anhui.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.anhui.chinatax.gov.cn:443",
    },
    {
        "code": "3500",
        "sfmc": "福建",
        "Ip": "https://fpcy.fujian.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.fujian.chinatax.gov.cn:443",
    },
    {
        "code": "3502",
        "sfmc": "厦门",
        "Ip": "https://fpcy.xiamen.chinatax.gov.cn/NWebQuery",
        "address": "https://fpcy.xiamen.chinatax.gov.cn",
    },
    {
        "code": "3600",
        "sfmc": "江西",
        "Ip": "https://fpcy.jiangxi.chinatax.gov.cn:82/NWebQuery",
        "address": "https://fpcy.jiangxi.chinatax.gov.cn:82",
    },
    {
        "code": "3700",
        "sfmc": "山东",
        "Ip": "https://fpcy.shandong.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.shandong.chinatax.gov.cn:443",
    },
    {
        "code": "3702",
        "sfmc": "青岛",
        "Ip": "https://fpcy.qingdao.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.qingdao.chinatax.gov.cn:443",
    },
    {
        "code": "4100",
        "sfmc": "河南",
        "Ip": "https://fpcy.henan.chinatax.gov.cn/NWebQuery",
        "address": "https://fpcy.henan.chinatax.gov.cn",
    },
    {
        "code": "4200",
        "sfmc": "湖北",
        "Ip": "https://fpcy.hubei.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.hubei.chinatax.gov.cn:443",
    },
    {
        "code": "4300",
        "sfmc": "湖南",
        "Ip": "https://fpcy.hunan.chinatax.gov.cn:8083/NWebQuery",
        "address": "https://fpcy.hunan.chinatax.gov.cn:8083",
    },
    {
        "code": "4400",
        "sfmc": "广东",
        "Ip": "https://fpcy.guangdong.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.guangdong.chinatax.gov.cn:443",
    },
    {
        "code": "4403",
        "sfmc": "深圳",
        "Ip": "https://fpcy.shenzhen.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.shenzhen.chinatax.gov.cn:443",
    },
    {
        "code": "4500",
        "sfmc": "广西",
        "Ip": "https://fpcy.guangxi.chinatax.gov.cn:8200/NWebQuery",
        "address": "https://fpcy.guangxi.chinatax.gov.cn:8200",
    },
    {
        "code": "4600",
        "sfmc": "海南",
        "Ip": "https://fpcy.hainan.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.hainan.chinatax.gov.cn:443",
    },
    {
        "code": "5000",
        "sfmc": "重庆",
        "Ip": "https://fpcy.chongqing.chinatax.gov.cn:80/NWebQuery",
        "address": "https://fpcy.chongqing.chinatax.gov.cn:80",
    },
    {
        "code": "5100",
        "sfmc": "四川",
        "Ip": "https://fpcy.sichuan.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.sichuan.chinatax.gov.cn:443",
    },
    {
        "code": "5200",
        "sfmc": "贵州",
        "Ip": "https://fpcy.guizhou.chinatax.gov.cn:80/NWebQuery",
        "address": "https://fpcy.guizhou.chinatax.gov.cn:80",
    },
    {
        "code": "5300",
        "sfmc": "云南",
        "Ip": "https://fpcy.yunnan.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.yunnan.chinatax.gov.cn:443",
    },
    {
        "code": "5400",
        "sfmc": "西藏",
        "Ip": "https://fpcy.xztax.gov.cn:81/NWebQuery",
        "address": "https://fpcy.xztax.gov.cn:81",
    },
    {
        "code": "6100",
        "sfmc": "陕西",
        "Ip": "https://fpcy.shaanxi.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.shaanxi.chinatax.gov.cn:443",
    },
    {
        "code": "6200",
        "sfmc": "甘肃",
        "Ip": "https://fpcy.gansu.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.gansu.chinatax.gov.cn:443",
    },
    {
        "code": "6300",
        "sfmc": "青海",
        "Ip": "https://fpcy.qinghai.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.qinghai.chinatax.gov.cn:443",
    },
    {
        "code": "6400",
        "sfmc": "宁夏",
        "Ip": "https://fpcy.ningxia.chinatax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.ningxia.chinatax.gov.cn:443",
    },
    {
        "code": "6500",
        "sfmc": "新疆",
        "Ip": "https://fpcy.xj-n-tax.gov.cn:443/NWebQuery",
        "address": "https://fpcy.xj-n-tax.gov.cn:443",
    },
]


# def get_flwq39(password):
#     public_key = """-----BEGIN PUBLIC KEY-----
#     MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCXY6ndiMJE7wF0qg9emVQik7FnCBidCr8V+yG/++iN/CwV0Rfe81wnjg2I23nbLJVuT63Y1T4x2etNr58BTHuzrCRy8gj3HPaS0GSGuiN7EWI1s0Bg6N78nvStPxeinyD8Qh3Bqa+5Z014nbOqn20kW4d3efLAeI7A6yc2uMPvfwIDAQAB
#     -----END PUBLIC KEY-----
#     """
#     rsakey = RSA.importKey(public_key)
#     cipher = Cipher_pksc1_v1_5.new(rsakey)
#     cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
#     return cipher_text.decode()
#

#
# def sectional_by_color(img, color):
#     """
#     把需要识别的字符转换成黑色，其他颜色都转换成白色
#
#     :param img: 图片
#     :param color: 颜色
#     :return:
#     """
#     pixdata = img.load()
#     for y in range(img.size[1]):
#         for x in range(img.size[0]):
#             pix = pixdata[x, y]
#             if color == "red":  # 255, 0, 0
#                 if pix[0] >= 128 and pix[1] < 128 and pix[2] < 128:
#                     pixdata[x, y] = (0, 0, 0)
#                 else:
#                     pixdata[x, y] = (255, 255, 255)
#             elif color == "yellow":  # 255, 255, 0
#                 if pix[0] > 128 and pix[1] > 128 and pix[2] < 128:
#                     pixdata[x, y] = (0, 0, 0)
#                 else:
#                     pixdata[x, y] = (255, 255, 255)
#             elif color == "blue":  # 0, 0, 255
#                 if pix[0] < 128 and pix[1] < 128 and pix[2] > 128:
#                     pixdata[x, y] = (0, 0, 0)
#                 else:
#                     pixdata[x, y] = (255, 255, 255)
#             else:  # 0, 0, 0
#                 if pix[0] < 128 and pix[1] < 128 and pix[2] < 128:
#                     pixdata[x, y] = (0, 0, 0)
#                 else:
#                     pixdata[x, y] = (255, 255, 255)
#     return img
#
#
# def base64_to_image(base64_str, color):
#     """
#     将 base64 字符串转换成图片
#     :param base64_str: base64 字符串
#     :param color: 颜色
#     :return:
#     """
#     base64_data = re.sub("^data:image/.+;base64,", "", base64_str)
#     byte_data = base64.b64decode(base64_data)
#     image_data = BytesIO(byte_data)
#     img = Image.open(image_data)
#     img = img.convert("RGB")
#     return sectional_by_color(img, color)


def init_js():
    with open("./crawler/main.js", "r") as f:
        jsfile = f.read()
    exjs = execjs.compile(jsfile)
    return exjs


def get_address(fpdm: str, **kwargs):
    """
    获取请求地址

    :param fpdm: 发票代码
    :param kwargs:
    :return:
    """
    if len(fpdm) == 12:
        dqdm = fpdm[1:5]
    else:
        dqdm = fpdm[:4]
    if dqdm not in ["2102", "3302", "3502", "3702", "4403"]:
        dqdm = dqdm[:2] + "00"
    for city in citys:
        if dqdm == city.get("code"):
            address = city.get("address")
    return address


def get_yzm(exjs, fpdm: str, fphm: str, address: str, **kwargs):
    """
    获取验证码

    :param exjs: 发票代码
    :param fpdm: 发票代码
    :param fphm: 发票号码
    :param address: 请求地址
    :param kwargs:
    :return:
    """
    nowtime = str(int(time.time() * 1000))
    key9 = exjs.call("key9", fpdm, fphm, nowtime)
    data = {
        "area": "undefined",
        "fpdm": fpdm,
        "fphm": fphm,
        "key9": key9,
        "nowtime": nowtime,
        "publickey": nowtime,
        "r": "0.1258228639153034",
        "v": "V2.0.04_004",
    }
    response = requests.post(
        url=f"{address}/NWebQuery/yzmQuery",
        headers={
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Dest": "script",
            "Referer": "https://inv-veri.chinatax.gov.cn/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
        },
        data=data,
        verify=False,
    )
    cookies = response.cookies.get_dict()["JSESSIONID"]
    if response.status_code == 200 and response.json():
        orgstr = response.json()["data"]
        result = exjs.call("replaceStr", orgstr, nowtime)
        if len(result) % 3 == 1:
            result += "=="
        elif len(result) % 3 == 2:
            result += "="
        str_obj = base64.b64decode(result).decode("utf-8")
        dict_obj = json.loads(str_obj)
        # key1 = dict_obj["key1"]
        yzmsj = dict_obj["key2"]
        index = dict_obj["key3"]
        color_num = dict_obj["key4"]
        color = None
        if color_num == "01":
            message = "请输入验证码图片中红色文字"
            color = "red"
        elif color_num == "02":
            message = "请输入验证码图片中黄色文字"
            color = "yellow"
        elif color_num == "03":
            message = "请输入验证码图片中蓝色文字"
            color = "blue"
        elif color_num == "00":
            message = "请输入验证码文字"
        else:
            message = "请重新获取验证码"
        # imgdata = base64.b64decode(key1)
        # file = open("img/origin.jpg", "wb")
        # file.write(imgdata)
        # file.close()
        # img = base64_to_image(base64_str=key1, color=color)
        # img.show()
        # img.save(f"img/{color}.jpg")
        # yzm = input(f"{message}：")
        yzm = get_aim_letters(dict_obj)
        return yzmsj, index, message, color, yzm, cookies
    else:
        raise


def main(fpdm: str, fphm: str, kprq: str, jym: str, address: str):
    """
    获取验证码

    :param fpdm: 发票代码
    :param fphm: 发票号码
    :param kprq: 开票日期
    :param jym: 校验码
    :param address: 请求地址
    :return:
    """
    exjs = init_js()
    yzmsj, index, message, color, yzm, cookies = get_yzm(exjs=exjs, fpdm=fpdm, fphm=fphm, address=address)
    cy_key9 = exjs.call("cykey9", fpdm, fphm, yzmsj)
    params = {
        "key1": fpdm,
        "key2": fphm,
        "key3": kprq,
        "key4": jym,
        "fplx": "10",
        "yzm": yzm,
        "yzmSj": yzmsj,
        "index": index,
        "area": "undefined",
        "publickey": yzmsj,
        "key9": cy_key9,
    }
    # new_url = "https://fpcy.zhejiang.chinatax.gov.cn/NWebQuery/vatQuery?" + parse.urlencode(params)
    # flwq39_password = exjs.call("vatQuery", {"type": "GET", "url": new_url})
    # flwq39 = get_flwq39(flwq39_password)
    # params["flwq39"] = flwq39
    response = requests.post(
        url=f"{address}/NWebQuery/vatQuery",
        headers={
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Dest": "script",
            "Referer": "https://inv-veri.chinatax.gov.cn/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": f"JSESSIONID={cookies}",
        },
        data=params,
        verify=False,
    ).json()
    stats = response.get("key1")
    if stats == "009":
        result = "查无此票"
    elif stats == "008":
        result = "验证码错误"
    elif stats == "007":
        result = "验证码失效"
    elif stats == "006":
        result = "不一致"
    elif stats == "005":
        result = "请求不合法"
    elif stats == "004":
        result = "超过服务器最大请求数，请稍后访问"
    elif stats == "003":
        result = "发票查验请求太频繁，请稍后再试"
    elif stats == "002":
        result = "超过该张发票当日查验次数(请于次日再次查验)"
    elif stats == "001":
        if response.get("key5") != "1":
            result = "系统异常，请重试！(07)"
        else:
            print("查询成功")
            result = response
            remark = response.get("key4").replace("≡", "\n")
            seller = response.get("key2").replace("≡", "\n")
            buy_info = response.get("key3").replace("≡", "\n")
            print(f"----------备注----------:\n{remark}")
            print(f"----------销售方----------:\n{seller}")
            print(f"----------发票信息----------:\n{buy_info}")
    elif stats == "rqerr":
        result = "当日开具发票可于次日进行查验"
    elif stats == "020":
        result = "由于查验行为异常，涉嫌违规，当前无法使用查验服务！"
    else:
        raise
    return result


if __name__ == "__main__":
    query_info = {
        "fpdm": "011001900511",  # 发票代码
        "fphm": "13093557",  # 发票号码
        "kprq": "20191111",  # 开票日期
        "jym": "821713",  # 校验码后 6 位
    }
    query_info["address"] = get_address(**query_info)
    result = main(**query_info)
    print(result)

# response = {
#     "key1": "001",
#     "key2": "4≡20191111≡江苏圆周电子商务有限公司北京分公司≡91110302585816506R≡北京经济技术开发区科创十一街18号C座2层223室 57807000≡交行北京海淀支行 110060576018150114912≡北方工业大学≡1211000040086596XB≡≡≡75477538000103821713≡0.00≡136.80≡≡661619994342≡136.80≡0≡≡",
#     "key3": "*印刷品*图书███0.000█186.80000000█186.80█1.00000000█0.00█1█1060201019900000000≡*印刷品*图书███0.000██-50.00██0.00█1█1060201019900000000",
#     "key4": "订单号:106611696343",
#     "key5": "1",
# }
