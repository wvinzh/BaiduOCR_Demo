# coding:utf-8
import urllib, base64
import urllib.request
import urllib.parse
import argparse
import os
import json

def ocr(img):
    res = ''
    access_token = '###your token####'
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
    # 二进制方式打开图文件
    f = open(img, 'rb')
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.parse.urlencode(params).encode("utf-8")
    request = urllib.request.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    if (content):
        print("success")
        content = json.loads(content)
        for word in content['words_result']:
            res += word['words']
    else:
        print("No Text Found")
    return res

parser = argparse.ArgumentParser("Baidu OCR")
parser.add_argument('--image_path', default='./images/', type=str, metavar='PATH',
                    help='path to the image')
parser.add_argument('--result_path', default='./result/', type=str, metavar='PATH',
                    help='path to the result')
args = parser.parse_args()
image_path = args.image_path
out_path = args.result_path
#scan image path
imgs = os.listdir(image_path)
for img in imgs:
    (filename,extension) = os.path.splitext(img)
    result_full_path = os.path.join(out_path,filename+'.txt')
    img_full_path = os.path.join(image_path,img)
    with open(result_full_path,'w') as f:
        f.write(ocr(img_full_path))


