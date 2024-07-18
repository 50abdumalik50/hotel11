# email_utils.py

# from django.conf import settings
# from oauthlib.oauth2 import BackendApplicationClient
# from requests_oauthlib import OAuth2Session
#
# def send_email_with_oauth2(subject, message, recipient):
#     client_id = '50a8735817fb4d96a9773e4c5229b626'
#     client_secret = '4d3b755cd7de4ed985958561032b4f65'
#     token_url = 'https://oauth.yandex.ru/token'
#
#     client = BackendApplicationClient(client_id=client_id)
#     oauth = OAuth2Session(client=client)
#     token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)
#
#     auth_string = f'Bearer {token["access_token"]}'
#     headers = {'Authorization': auth_string}
#
#     response = oauth.post(settings.EMAIL_HOST, headers=headers, data={
#         'from': settings.DEFAULT_FROM_EMAIL,
#         'to': recipient,
#         'subject': subject,
#         'text': message
#     })
#
#     if response.status_code == 200:
#         print('Email sent successfully!')
#     else:
#         print('Failed to send email.')
#
#     # Создание клиента OAuth2
#     client = BackendApplicationClient(client_id=client_id)
#     oauth = OAuth2Session(client=client)
#
#     # Получение токена доступа
#     token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)
#
#     # Формирование заголовков для авторизации
#     auth_string = f'Bearer {token["access_token"]}'
#     headers = {'Authorization': auth_string}
#
#     try:
#         # Отправка письма через Yandex SMTP
#         response = oauth.post('https://smtp.yandex.com/api/v1/messages/send', headers=headers, json={
#             'from': settings.DEFAULT_FROM_EMAIL,
#             'to': recipient,
#             'subject': subject,
#             'text': message,
#         })
#
#         if response.status_code == 200:
#             print('Email sent successfully!')
#         else:
#             print(f'Failed to send email. Status code: {response.status_code}')
#     except Exception as e:
#         print(f'Error sending email: {str(e)}')
#
#
# # Пример использования
# send_email_with_oauth2('Тестовое письмо', 'Привет, это тестовое письмо.', 'abdumalik50@yandex.ru')