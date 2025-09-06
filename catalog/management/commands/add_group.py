from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        permissions = Permission.objects.filter(codename__in=['can_unpublish_product', 'delete_product'])
        group.permissions.set(permissions)
        self.stdout.write(self.style.SUCCESS('Successfully created group "Модератор продуктов"'))