from django.db import models
from django.utils import timezone

# Create your models here.
class My_books(models.Model):
	title=models.CharField('Заголовок', max_length=100)
	content=models.TextField('Описание')
	tpublish=models.DateTimeField('Дата публикации',default=timezone.now)

	class Meta:
		verbose_name='Книга'
		verbose_name_plural='Книги'

	def __str__(self):
		return self.title
	def __unicode__(self):
		return self.title