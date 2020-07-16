from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    title = models.CharField(max_length=30)
    message = models.TextField(max_length=1000)
    date_created = models.DateTimeField(verbose_name="Date Submission", auto_now_add="True")

    class Meta:
        db_table = "Contact Form Table"
        verbose_name = "Contact Request"
        verbose_name_plural = "Contact Requests"


