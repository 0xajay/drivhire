import requests

url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message=This%20is%20a%20test%20message&language=english&route=p&numbers=9008785654"
headers = {
    'authorization': "Ek5wWht2O4jxfFunAGIX7qdDN9Tg3YLl0seSCvaobUMy18B6PrFyPDVedRQs2GHtao39vl6hrn8uTEKS",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }


def send_sms(message, phone_number):
    try:
        payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+phone_number
        response = requests.request("POST", url, data=payload, headers=headers)
    except Exception as err:
        raise Exception(err)
