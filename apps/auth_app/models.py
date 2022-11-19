from django.db import models

from django.contrib.auth.models import AbstractUser

from imagekit import models as image_models
from imagekit import processors as image_proc

from .enums import SEX


class User(AbstractUser):

    SEX_CHOICES = (
        (SEX.MASCULINE, "Masculino"),
        (SEX.FEMININE, "Feminino"),
    )

    sex = models.CharField(
        max_length=1, choices=SEX_CHOICES, null=True, blank=True, verbose_name="Sexo"
    )

    phone = models.CharField(
        max_length=14, null=True, blank=True, verbose_name="Telefone"
    )

    birthday_date = models.DateField(
        null=True, blank=True, verbose_name="Data de nascimento"
    )

    picture = models.ImageField(upload_to="accounts/%Y/%m/%d", null=False, blank=True)

    picture_thumb = image_models.ImageSpecField(
        source="picture",
        processors=[image_proc.ResizeToFit(200, 200)],
        format="JPEG",
        options={"quality": 60},
    )
