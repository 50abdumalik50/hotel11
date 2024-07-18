# from django.core.mail import send_mail
# from django.conf import settings
#
# # send_mail(
# #     'Subject here',
# #     'Here is the message.',
# #     settings.DEFAULT_FROM_EMAIL,
# #     ['abdumalik50@yandex.ru'],  # Замените на адрес получателя
# #     fail_silently=False,
# # )
#
#
# send_mail(
#     'Test Email',
#     'Congratulations you book a room.',
#     settings.DEFAULT_FROM_EMAIL,
#     ['abdumalik50@yandex.ru'],  # Замените на email получателя
#     fail_silently=False,
# )

from django.core.mail import send_mail

subject = 'Test Email'
message = 'This is a test email sent using SMTP in Django.'
from_email = 'abdumalikabdukarimov50@gmail.com'
recipient_list = ['srojiddin4879@icloud.com']

send_mail(subject, message, from_email, recipient_list)