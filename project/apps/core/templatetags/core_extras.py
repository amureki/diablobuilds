# -*- coding:utf-8 -*-
import re
from django import template

register = template.Library()


@register.filter
def battletag(name):
    regex = re.compile(r'^[a-zA-Z0-9]{3,12}#[0-9]{4}$')
    if regex.match(name):
        url = re.sub('[#]', '-', name)
        return u'<a href="http://battle.net/d3/profile/%s/">%s</a>' % (url, name)
    return None