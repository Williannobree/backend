
from django.db import models

class plantio(models.Model):
    id = models.CharField(max_length=100)
    def __str__(self):
        return self.id

        from django.db import models

class propriedade(models.Model):
    id = models.CharField(max_length=100)
    def __str__(self):
        return self.id

        from django.db import models

class cultura(models.Model):
    id = models.CharField(max_length=100)
    def __str__(self):
        return self.id

        from django.db import models

class data_plantio(models.Model):
    data = models.CharField(max_length=50)
    def __str__(self):
        return self.data

  from django.db import models

       class area_plantada (models.Model):
    area = models.CharField(max_length=50)
    def __str__(self):
        return self.area

        from django.db import models

class status (models.Model):
    status = models.CharField(max_length=50)
 
    def __str__(self):
        return self.status
