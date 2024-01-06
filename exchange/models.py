from django.db import models


class Exchange(models.Model):
    key = models.CharField(max_length=200, blank=False, null=False)
    id_object = models.IntegerField(blank=False, null=False)
    action = models.CharField(max_length=50)

    class Meta:
        unique_together = (("key", "id_object",),)

    
    def __str__(self):
        return f"{self.id}. {self.key}({self.id_object} [{self.action}])"