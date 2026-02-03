from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название покемона')
    image = models.ImageField(upload_to='pokemons_image/', verbose_name='Изображение покемона', blank=True, null=True)
    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Дата появления покемона', blank=True, null=True)
    disappeared_at = models.DateTimeField(verbose_name='Дата исчезновения покемона', blank=True, null=True)
    def __str__(self):
        return self.pokemon
