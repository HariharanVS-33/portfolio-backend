from django.db import models

class Skill(models.Model):
    category = models.CharField(max_length=100, help_text="Category name e.g. Frontend, Backend, Tools")
    name = models.CharField(max_length=100, help_text="Skill name e.g. React, Python, Git")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"
