from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название покемона')
    image = models.ImageField(upload_to='pokemons_image/', verbose_name='Изображение покемона', blank=True, null=True)
    def __str__(self):
        return self.title