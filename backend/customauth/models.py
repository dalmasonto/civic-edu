from django.db import models
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMultiAlternatives


# Create your models here.
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
    #                                                reset_password_token.key)

    # print(f"\nReset password {reset_password_token.key}\n")
    # sendepasswordresetmail(reset_password_token.user, reset_password_token.key)

    ctx = {
        'name': reset_password_token.user.get_full_name(),
        'username': reset_password_token.user.username,
        'reset_password_url': f'https://rhea.africa/auth/password/confirm/?token={reset_password_token.key}',
        'token': reset_password_token.key}

    html_content = render_to_string("reset-password.html", context=ctx)
    text_content = strip_tags(html_content)

    email_text = EmailMultiAlternatives(
        'Rhea - Reset Password',
        text_content,
        f'Rhea Africa <noreply@supercodehive.com>',
        [reset_password_token.user.email],
        reply_to=['Rhea Africa <info@rhea.africa>']
    )

    email_text.attach_alternative(html_content, 'text/html')
    email_text.send()
