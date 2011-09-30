#coding: utf-8

from django.db import models
from django.conf import settings
from fields import BigAutoField
from django.db.backends import signals

class Active(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    time = models.IntegerField(null=True)

    class Meta:
        db_table = u'active'

class Authreg(models.Model):
    username = models.CharField(max_length = 255, db_index=True, null=True)
    realm = models.CharField(max_length=255, db_index=True, null=True)
    password = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'authreg'
        unique_together = ("username", "realm")

class DiscoItems(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    jid = models.TextField(null=True)
    name = models.TextField(null=True)
    node = models.TextField(null=True)

    class Meta:
        db_table = 'disco-items'

class Logout(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    time = models.IntegerField(null=True)

    class Meta:
        db_table = u'logout'

class MotdMessage(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    xml = models.TextField(null=True)
    
    class Meta:
        db_table = u'motd-message'

class MotdTimes(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    time = models.IntegerField(null=True)

    class Meta:
        db_table = u'motd-times'

class PrivacyDefault(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    default = models.TextField(null=True)

    class Meta:
        db_table = u'privacy-default'

class PrivacyItems(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    itemlist = models.TextField(db_column='list', null=True)
    itemtype = models.TextField(db_column='type', null=True)
    value = models.TextField(null=True)
    deny = models.SmallIntegerField(null=True)
    order = models.IntegerField(null=True)
    block = models.IntegerField(null=True)    
    
    class Meta:
        db_table = u'privacy-items'

class Private(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    ns = models.TextField(null=True)
    xml = models.TextField(null=True)

    class Meta:
        db_table = u'private'

class Queue(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    xml = models.TextField(null=True)

    class Meta:
        db_table = u'queue'

class RosterGroups(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    jid = models.TextField(null=True)
    group = models.TextField(null=True)
    
    class Meta:
        db_table = u'roster-groups'

class RosterItems(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    jid = models.TextField(null=True)
    name = models.TextField(null=True)
    item_to = models.SmallIntegerField(db_column='to', null=True)
    item_from = models.SmallIntegerField(db_column='from', null=True)
    ask = models.IntegerField(null=True)
    
    class Meta:
        db_table = u'roster-items'

class Status(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    status = models.TextField()
    show = models.TextField()
    last_login = models.IntegerField(db_column = 'last-login', null=True, default=0)
    last_logout = models.IntegerField(db_column = 'last-logout', null=True, default=0)
    xml = models.TextField(null=True)
    
    class Meta:
        db_table = u'status'

class VacationSettings(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    message = models.TextField(null=True)
    
    class Meta:
        db_table = u'vacation-settings'

class Vcard(models.Model):
    owner = models.CharField(db_column='collection-owner', db_index = True, max_length=255)
    objid = BigAutoField(db_column='object-sequence', primary_key = True)
    fn = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    jabberid = models.CharField(max_length=3071, null=True)
    mailer = models.CharField(max_length=1023, null=True)
    title = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=255, null=True)
    bday = models.CharField(max_length=255, null=True)
    tz = models.CharField(max_length=7, null=True)
    n_family = models.CharField(db_column='n-family', max_length=255, null=True)
    n_given = models.CharField(db_column='n-given', max_length=255, null=True)
    n_middle = models.CharField(db_column='n-middle', max_length=255, null=True)
    n_prefix = models.CharField(db_column='n-prefix', max_length=255, null=True)
    n_suffix = models.CharField(db_column='n-suffix', max_length=255, null=True)
    adr_street = models.CharField(db_column='adr-street', max_length=255, null=True)
    adr_extadd = models.CharField(db_column='adr-extadd', max_length=255, null=True)
    adr_pobox = models.CharField(db_column='adr-pobox', max_length=15, null=True)
    adr_locality = models.CharField(db_column='adr-locality', max_length=255, null=True)
    adr_region = models.CharField(db_column='adr-region', max_length=255, null=True)
    adr_pcode = models.CharField(db_column='adr-pcode', max_length=31, null=True)
    adr_country = models.CharField(db_column='adr-country', max_length=63, null=True)
    geo_lat = models.CharField(db_column='geo-lat', max_length=255, null=True)
    geo_lon = models.CharField(db_column='geo-lon', max_length=255, null=True)
    org_orgname = models.CharField(db_column='org-orgname', max_length=255, null=True)
    org_orgunit = models.CharField(db_column='org-orgunit', max_length=255, null=True)
    agent_extval = models.CharField(db_column='agent-extval', max_length=255, null=True)
    sort_string = models.CharField(db_column='sort-string', max_length=255, null=True)
    desc = models.TextField(null=True)
    note = models.TextField(null=True)
    uid = models.CharField(db_column='uid', max_length=255, null=True)
    photo_type = models.CharField(db_column='photo-type', max_length=127, null=True)
    photo_binval = models.TextField(db_column='photo-binval', null=True)
    photo_extval = models.CharField(db_column='photo-extval', max_length=255, null=True)
    logo_type = models.CharField(db_column='logo-type', max_length=127, null=True)
    logo_binval = models.TextField(db_column='logo-binval', null=True)
    logo_extval = models.CharField(db_column='logo-extval', max_length=255, null=True)
    sound_phonetic = models.CharField(db_column='sound-phonetic', max_length=255, null=True)
    sound_binval = models.TextField(db_column='sound-binval', null=True)
    sound_extval = models.CharField(db_column='sound-extval', max_length=255, null=True)
    key_type = models.CharField(db_column='key-type', max_length=127, null=True)
    key_cred = models.TextField(db_column='key-cred', null=True)
    rev = models.CharField(db_column='rev', max_length=255, null=True)

    class Meta:
        db_table=u'vcard'


def migrate_hosts(*args, **kwargs):
    def change(jid):
        return '%s@%s' % (jid.split('@')[0], settings.DOMAIN)

    try:
        for item in Authreg.objects.all():
            item.realm = settings.DOMAIN
            item.save()

        for item in Active.objects.all():
            item.owner = change(item.owner)
            item.save()

        for item in RosterItems.objects.all():
            item.owner = change(item.owner)
            item.jid = change(item.jid)
            item.save()

        for item in RosterGroups.objects.all():
            item.owner = change(item.owner)
            item.jid = change(item.jid)
            item.save()
    except Exception:
        #acontece quando a tabela não existe.
        #melhor deixar um exception generico, isso nao é importante        
        pass 

#signals.connection_created.connect(migrate_hosts)
    
