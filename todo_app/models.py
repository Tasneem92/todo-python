from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Todo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=256)
    description = models.TextField(db_column='Description', unique=True)

    class Meta:
        managed = True
        db_table = "Todo"

    def get_absolute_url(self):
     return reverse('todo_app:post_detail', args=[self.id])


class TodoMirror(models.Model):
    id = models.OneToOneField(Todo,primary_key=True)
    mname = models.ForeignKey(Todo,to_field="name",related_name='titles')
    mdescription = models.ForeignKey(Todo,to_field="description",related_name='posts')

    class Meta:
        managed = True
        db_table = 'TodoMirror'
