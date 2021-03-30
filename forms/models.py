from django.db import models


class UserInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=20)
    registration_date = models.DateTimeField('date published')

    def __str__(self):
        return '|{: <20}|{: <20}|{: <20}|{: <20}|'.format(
                # self.id,
                self.first_name,
                self.last_name,
                self.user_email,
                str(self.registration_date)
                )
