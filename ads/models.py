from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    """
    Модель для сущности - объявление
    """
    title = models.CharField(max_length=200, verbose_name='название')
    price = models.PositiveIntegerField(verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='ad_owner',
                               verbose_name='автор', **NULLABLE)
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата')

    def __str__(self):
        return f'{self.title} цена: {self.description} '

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ['-created_at']


class Review(models.Model):
    """
    Модель для сущности - отзыв
    """
    text = models.TextField(verbose_name='текст отзыва')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление', related_name='review_ad')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='review_owner',
                               verbose_name='автор отзыва', **NULLABLE)
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата публиувции отзыва')

    def __str__(self):
        return f'{self.text} {self.author}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
