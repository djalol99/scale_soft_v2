from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from exchange.models import Exchange


list_modules = ["catalogs.models", "documents.models"]

@receiver(post_save)
def note_action(sender, instance, created, **kwargs):
    if not sender.__module__ in list_modules:
        return
    
    key = sender.__module__ + "." + sender.__name__
    
    result = Exchange.objects.filter(key=key, id_object=instance.id).first()
    if result:
        return

    if created:
        action = "created"
    else:
        action = "updated"
    
    Exchange.objects.create(key=key, id_object=instance.id, action=action)

@receiver(post_delete)
def note_action(sender, instance, **kwargs):
    if not sender.__module__ in list_modules:
        return
    
    key = sender.__module__ + "." + sender.__name__
    action = "deleted"

    result = Exchange.objects.filter(key=key, id_object=instance.id).first()
    if result:
        result.action = action
        result.save()
    else:
        Exchange.objects.create(key=key, id_object=instance.id, action=action)
