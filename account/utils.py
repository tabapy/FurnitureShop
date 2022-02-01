from django.core.mail import send_mail


def send_welcome_email(email):
    message = f'Dear {email}, thank you for registration on our site FurnitureShop!'
    send_mail(
        'Welcome to FurnitureShop!',
        message,
        'burgerkingadmin@burger.net',
        [email],
        fail_silently=False
    )
