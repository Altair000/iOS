# Módulos de python
import base64

def captcha_solver(session, session_id, widget_key, scnt):
    captcha_data = {
        'type': 'IMAGE',
        }

    captcha_headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://appleid.apple.com',
        'Referer': 'https://appleid.apple.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
        'X-Apple-I-TimeZone': 'America/Havana',
        'X-Apple-ID-Session-Id': session_id,
        'X-Apple-Request-Context': 'create',
        'X-Apple-Widget-Key': widget_key,
        'scnt': scnt,
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        }

    captcha = session.post('https://appleid.apple.com/captcha', json=captcha_data, headers=captcha_headers, impersonate='safari')
    captcha_json = captcha.json()
    captcha_img_encodec = captcha_json['payload']['content']
    captcha_img_decodec = base64.b64decode(captcha_img_encodec)
    with open('captcha.jpg', 'wb') as captcha_file:
        captcha_file.write(captcha_img_decodec)

    captcha = input("Introduzca el valor de la imagen captcha: ")
    captcha_token = captcha_json["token"]
    captcha_id = captcha_json["id"]

    return captcha_id, captcha_token, captcha