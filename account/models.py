from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'


class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

m2m = models.ManyToManyField(User, through=Contact, related_name='followers', symmetrical=False)

User.add_to_class('following', m2m)

def get_absolute_url(self):
    return reverse('user_detail', args=[self.username])
    
    
User.add_to_class('get_absolute_url', get_absolute_url)


