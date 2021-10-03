# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import cv2
import base64
import argparse


def get_token(client_id: str, client_secret: str):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+ client_id + '&client_secret=' + client_secret
    response = requests.get(host)
    print("token:", response.json())
    return response.json()["access_token"]


def request(template_base64: str, target_base64: str, access_token: str):
    param = {
        "version": "4.0",
        "image_template": {
            "image": template_base64,
            "image_type": "BASE64",
        },
        "image_target": {
            "image": target_base64,
            "image_type": "BASE64",
        },
        "merge_degree": "COMPLETE"
    }

    param = json.dumps(param)

    request_url = "https://aip.baidubce.com/rest/2.0/face/v1/merge"

    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=param, headers=headers)

    return response.json()


def read_resize_encode_base64(image_path: str):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (1920, 1080))
    img_str = cv2.imencode('.jpg', img)[1].tostring()
    b64_code = base64.b64encode(img_str)
    return b64_code


def argsParse():
    parser = argparse.ArgumentParser(description='这是给羽觞觞的百度人脸合成调用器， 你只需要按说明填好下面的参数即可')

    # 添加参数步骤
    parser.add_argument('template', type=str,
                        help='把谁的脸融合上去')
    parser.add_argument('target', type=str,
                        help='融合到谁的脸上')
    parser.add_argument('--client_id', type=str, help="从官网拿到的client_id", dest='ak',
                        default="f91e6f1d180643f68b1aae900d35e113")
    parser.add_argument('--client_secret', type=str, help="从官网拿到的client_secret", dest='ck',
                        default="0f99211cfd1a4d3e84682ef8f1f580d1")
    # 解析参数步骤
    args = parser.parse_args()
    return args


def main():
    args = argsParse()
    print(args)
    token = get_token(args.ak, args.ck)
    response = request(read_resize_encode_base64(args.template),
                       read_resize_encode_base64(args.target),
                       token)
    if response["error_code"] == 0:
        img = base64.b64decode(response["result"]["merge_image"])
        with open("./result.jpg", 'wb') as f:
            f.write(img)
    else:
        print(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
