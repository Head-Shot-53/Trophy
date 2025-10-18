from django.db import models

class Platform(models.Model):
    PLATFORM = [
        ('PC', 'Computer'),
        ('PS5', 'Play Station 5'),
        ('PS4', 'Play Station 4'),
        ('XBOX', 'XBOX'),
        ('SWITCH', 'Nintendo Switch')
    ]

    name = models.CharField(max_length=20, choices=PLATFORM, unique=True, verbose_name='Платформа')

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформи'

    def __str__(self):
        return self.get_name_display()

class Game(models.Model):

    DIFFICULT_ACHIEVEMENTS = [
        ('Difficult', 'Складно'),
        ('Medium', 'Середньо'),
        ('Easy', 'Легко')
    ]

    title = models.CharField(max_length=250, verbose_name='Назва гри')
    slug = models.SlugField(unique=True, max_length=255, verbose_name='URL гри')
    platform = models.ManyToManyField(Platform,verbose_name='Платформа', related_name='games')
    genre = models.CharField(max_length=100, verbose_name='Жанр гри')
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to='game_images/', default='default_image.png', blank=True, verbose_name='Картинка гри')
    description = models.TextField(verbose_name='Опис гри')
    developer = models.CharField(max_length=150, blank=True, verbose_name='Розробник')
    publisher = models.CharField(max_length=150, blank=True, verbose_name='Видавець')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    difficulty = models.CharField(choices=DIFFICULT_ACHIEVEMENTS, verbose_name='Складність досягнень', max_length=10, default='Medium')

    class Meta:
        verbose_name = 'Гра'
        verbose_name_plural = 'Ігри'
        ordering = ['-title']

    def __str__(self):
        return self.title
    

