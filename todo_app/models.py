from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Todo(models.Model):
    name = models.CharField(db_column='Name', max_length=50)
    description = models.TextField(db_column='Description',max_length=150)

    class Meta:
        managed = True
        db_table = "Todo"

    def get_absolute_url(self):
     return reverse('todo_app:post_detail', args=[self.id])

    def __str__(self):
        return self.name

class TodoMirror(models.Model):
    id = models.OneToOneField(Todo,primary_key=True, on_delete=models.CASCADE)
    mname = models.CharField(max_length=50, blank=True)
    mdescription = models.TextField(max_length=150, blank=True)

    class Meta:
        managed = True
        db_table = 'TodoMirror'

    def __str__(self):
        return self.mname

@receiver(post_save, sender=Todo)
def create_mirror_obj(sender, instance, created, **kwargs):
    if created:
        obj = TodoMirror.objects.create(id=instance,mname=instance.name,
                                    mdescription=instance.description)
        obj.save()
    if not created:
        TodoMirror.objects.filter(id=instance).update(mname=instance.name)
        TodoMirror.objects.filter(id=instance).update(mdescription=instance.description)
        pass

@receiver(post_save, sender=TodoMirror)
def create_todo_obj(sender, instance, created, **kwargs):
    if created:
        obj = Todo.objects.create(name=instance.mname,
                                    description=instance.mdescription)
        obj.save()
    if not created:
        Todo.objects.filter(id=instance.id.id).update(name=instance.mname)
        Todo.objects.filter(id=instance.id.id).update(description=instance.mdescription)
        pass

@receiver(post_delete, sender=TodoMirror)
def delete_todo_obj(sender, instance, **kwargs):
    obj = Todo.objects.get(id=instance.id.id)
    obj.delete()
