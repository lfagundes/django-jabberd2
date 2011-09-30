# -*- coding: utf-8 -*-

from django.db.models import fields
from south.modelsinspector import add_introspection_rules

# This BigAutoField is only implemented to work with MySQL. If you use other database, either implement it below or use AutoField instead.

class BigAutoField(fields.BigIntegerField):
    def db_type(self, connection):
        module = connection.__class__.__module__
        if 'mysql' in module:
            return 'bigint AUTO_INCREMENT'
        elif 'sqlite' in module:
            return 'integer'
        return super(BigAutoField, self).db_type()        

add_introspection_rules([], ["^jabber\.fields\.BigAutoField"])
