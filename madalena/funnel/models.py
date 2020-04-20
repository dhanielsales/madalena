from django.db import models
from django.dispatch import receiver

class EntryImagesManager(models.Manager):

    def define_resized(self, id):
        resized_item = self.get(id=id)
        resized_item.resized = True
        resized_item.save()

        return True

class EntryImages(models.Model):

    id = models.AutoField('Id', primary_key=True)
    added_at = models.DateTimeField('Adicionada em', auto_now_add=True)
    modified = models.DateTimeField('Modificada em', auto_now=True)
    image = models.ImageField('Imagem de entrada', upload_to='entry_images', blank=False, null=False)
    crop = models.BooleanField('Cortar', default=True)
    resized = models.BooleanField('Redimencionada', default=False)
    height = models.PositiveIntegerField('Altura', default=384, blank=False, null=False)
    width = models.PositiveIntegerField('Largura', default=384, blank=False, null=False)

    objects = EntryImagesManager()

    class Meta:
        verbose_name = 'Imagem de entrada'
        verbose_name_plural = "Imagems de entradas"
        ordering = ['added_at']

    def __str__(self):
        return f'{self.image}'

@receiver(models.signals.post_save, sender=EntryImages)
def task_resizer_call(sender, instance, created, **kwargs):
    print(instance.image.url)
    print(type(instance.image))

