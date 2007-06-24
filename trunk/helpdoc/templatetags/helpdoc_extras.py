from django import template
from django.db.models import get_apps
from django.core.urlresolvers import reverse
import os.path
import re

register = template.Library()

def title(content, site_title=None):
    """
    #title = re.match('(<.*?>)*(?P<title>[^<]+).*', content).group("title")
    (?<|>)[^<]+
    (<.*?>)*(?P<title>[^<]+).*
    (<[^>]>)
    <P/>
    (?>=>).*(?=</)
    """
    title = None
    try:
        from BeautifulSoup import BeautifulSoup
        title = BeautifulSoup(content).find("h1")
        if title:
            while True:
                try:
                    title = title.contents[0]
                except (KeyError, AttributeError):
                    break
    except ImportError:
        try:
            from lxml import etree
            parser = etree.HTMLParser()
            title = etree.fromstring(content, parser).xpath("//h1/a")[0].text
        except ImportError:
            pass
    
    if title:
        title = title.encode("UTF-8")
    else:
        title = "Not Found Title Line."
    if site_title and (not title == site_title):
        title += " : %s" % site_title
    return title
register.simple_tag(title)

def get_app_list():
    app_list = {}
    for app in get_apps():
        if os.path.exists(os.path.join(os.path.dirname(app.__file__), 'docs')):
            app_list[app.__name__.split(".")[-2]] = os.path.dirname(app.__file__)
    return app_list

def app_menu():
    return dict(app_list=get_app_list())
register.inclusion_tag("tags/app_menu.html")(app_menu)

def app_list():
    return dict(app_list=get_app_list())
register.inclusion_tag("tags/app_list.html")(app_list)

def admin_base_url():
    return reverse('django.contrib.admin.views.main.index')
register.simple_tag(admin_base_url)
