from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название покемона на русском', default='-')
    title_en = models.CharField(max_length=200, verbose_name='Название покемона на английском', default='-')
    title_jp = models.CharField(max_length=200, verbose_name='Название покемона на японском', default='-')
    image = models.ImageField(upload_to='pokemons_image/', verbose_name='Изображение покемона', blank=True, null=True)
    evolution_from = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name='От кого эволюционировал', related_name = 'next_evolution', blank=True, null=True)
    description = models.TextField(verbose_name='Описание покемона', default='') 
    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Дата появления покемона', blank=True, null=True)
    disappeared_at = models.DateTimeField(verbose_name='Дата исчезновения покемона', blank=True, null=True)
    level = models.CharField(max_length=2, verbose_name='Уровень', default='1')
    health = models.CharField(max_length=2, verbose_name='Здоровье', default='10')
    strength = models.CharField(max_length=2, verbose_name='Сила', default='5')
    defence = models.CharField(max_length=2, verbose_name='Защита', default='5')
    stamina = models.CharField(max_length=2, verbose_name='Выносливость', default='5')