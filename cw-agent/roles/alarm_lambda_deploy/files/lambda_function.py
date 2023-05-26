# for telegram lambda template integration with cloudwatch alarm
import requests
def lambda_handler(event, context):
    # prepare message for alarm
    message = {}
    if event.get('id'):
        message["id"] = event['id']
    if event.get('detail').get('alarmName'):
        message["name"] = event['detail']['alarmName']
    if event.get('time'):
        message["time"] = event['time']
    if event.get('detail').get('state') and event.get('detail').get('state').get('value'):
        message["status"] = event.get('detail').get('state').get('value')
    if event.get('detail').get('state') and event.get('detail').get('state').get('reason'):
        message["reason"] = event.get('detail').get('state').get('reason')

    # set telegram configuration

    channel_id = f"<your_telegram_chat_id>"
    bot_url_prefix = f"https://api.telegram.org/bot<your_telegram_bot_token>/sendMessage"

    # set request
    text = f"""
    <b>{message['name']}</b>
    ==============================
    "狀態": <code>{message['status']}</code>
    "時間": <code>{message['time']}</code>
    "內容": <code>{message['reason']}</code>
    "ID": <code>{message['id']}</code>
    """
    
    h = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    b = {
        "chat_id": f"{channel_id}",
        "text": f"{text}",
        "parser_mode": "HTML",
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": None
    }

    requests.post(url=f"{bot_url_prefix}", headers=h, json=b)
    return message