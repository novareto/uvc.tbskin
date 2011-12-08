# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

import grok

from zope.interface import Interface
from megrok import resourceviewlet
from fanstatic import Library, Resource
from js.bootstrap import bootstrap

library = Library('nva.tbskin', 'static')
main_css = Resource(library, 'main.css')


class TBSkinViewlet(resourceviewlet.ResourceViewlet):
    grok.context(Interface)
    resources = [main_css, bootstrap]

    def update(self):
        [x.need() for x in self.resources]



#
### Examples
#

import uvcsite
from zope import interface, schema

grok.templatedir('templates')


class Index(uvcsite.Page):
    grok.context(interface.Interface)

class HTMLTags(uvcsite.Page):
    grok.context(interface.Interface)


class AppsExample(uvcsite.SubMenu):
    grok.title('Applications')
    grok.context(interface.Interface)
    grok.viewletmanager(uvcsite.IGlobalMenu)

    action = "lars"

class App1(uvcsite.MenuItem):
    grok.title('Application One')
    grok.viewletmanager(AppsExample)

    action = u"myform"

class IPerson(interface.Interface):

    id = schema.TextLine(
       title = u"Id",
       description = u"Not more then 3 letters",
       max_length=3,
       )

    name = schema.TextLine(
       title = u"Name",
       description = u"Please give your first name Here",
       )

class MyForm(uvcsite.Form):
    grok.context(interface.Interface)
    fields = uvcsite.Fields(IPerson)

    label = u"LABEL"
    description = u"DEscription"

    @uvcsite.action('Save')
    def handle_save(self):
        data, errors = self.extractData()
        if errors:
            self.flash(u'Damn a Error')
            return
        self.flash(u'Success')


class LoggedinAs(uvcsite.MenuItem):
    grok.context(interface.Interface)
    grok.viewletmanager(uvcsite.IPersonalPreferences)
    
    @property
    def title(self):
        return "You are logged in as MASTER"


