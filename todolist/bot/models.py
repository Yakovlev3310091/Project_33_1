from django.db import models


class TgUser(models.Model):

    class Meta:
        pass

    chat_id = models.CharField(verbose_name="id чата", max_length=255)
    user_id = models.CharField(verbose_name="id пользователя", max_length=255)
    user = models.ForeignKey("core.User", verbose_name="Пользователь", on_delete=models.PROTECT, null=True, blank=True)
    verification_code = models.CharField(verbose_name="Код верификации", max_length=255, null=True, blank=True)



