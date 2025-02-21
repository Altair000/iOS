# Módulos de python
import json
# Módulos Locales
from utils.captcha import captcha_solver
# Módulos de terceros
from curl_cffi import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = 'https://appleid.apple.com/'

home = session.get(url, impersonate='safari')

widget_key = session.get('https://account.apple.com/bootstrap/portal', impersonate='safari')
widget_key_json = widget_key.json()

widget_key = widget_key_json["serviceKey"]

nexxt = session.get(f'https://appleid.apple.com/widget/account/?roleType=Agent&lv=0.3.17&widgetKey={widget_key}&v=3&appContext=account', impersonate='safari')

soup = BeautifulSoup(nexxt.content, 'html.parser')
target_script = soup.find('script', {'type': 'application/json', 'id': 'boot_args'})
data = json.loads(target_script.string)

session_id = data["direct"]["sessionId"]
scnt = data["direct"]["scnt"]

captcha_id, captcha_token, captcha = captcha_solver(session, session_id, widget_key, scnt)

country_select = session.get('https://appleid.apple.com/account?countryCode=USA', impersonate='safari')

apple_id_verify_data = {
    'emailAddress': 'pepejuan143@gmail.com',
}

apple_id_verify = session.post('https://appleid.apple.com/account/validation/appleid', data=apple_id_verify_data, impersonate='safari')

password_validate_data = {
    'password': '&802r4rL',
    'accountName': 'pepejuan143@gmail.com',
    'updating': False,
}

password_validate = session.post('https://appleid.apple.com/account/validate/password', data=password_validate_data, impersonate='safari')

validate_data = {
    'phoneNumberVerification': {
        'phoneNumber': {
            'id': 1,
            'number': '(815) 486-0694',
            'countryCode': 'US',
            'countryDialCode': '1',
            'nonFTEU': True,
        },
        'mode': 'sms',
    },
    'account': {
        'name': 'delatorremanfred@gmail.com',
        'password': 'TumnK&C8',
        'person': {
            'name': {
                'firstName': 'Raydiel',
                'lastName': 'Espinosa',
            },
            'birthday': '2006-06-04',
            'primaryAddress': {
                'country': 'USA',
            },
        },
        'preferences': {
            'preferredLanguage': 'es_MX',
            'marketingPreferences': {
                'appleNews': False,
                'appleUpdates': False,
                'iTunesUpdates': False,
            },
        },
        'verificationInfo': {
            'id': '',
            'answer': '',
        },
    },
    'captcha': {
        'id': captcha_id,
        'token': captcha_token,
        'answer': captcha,
    },
    'privacyPolicyChecked': False,
}

validate_headers = {
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

validate = requests.post('https://appleid.apple.com/account/validate', json=validate_data, headers=validate_headers, impersonate='safari')

print(validate.status_code)
print(validate.json())