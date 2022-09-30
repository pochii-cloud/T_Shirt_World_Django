from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.EmailField(max_length=1000)

    def __str__(self):
        return self.name

    def save_contacts(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    class Meta:
        verbose_name_plural = 'Contacts'
