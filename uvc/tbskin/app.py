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

    def update1(self):
        self.flash('Normal')
        self.flash('Warning', type="success")
        self.flash('Error', type="error")
        self.flash('Info', type="info")

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



class MyFormHelp(uvcsite.HelpPage):
    grok.context(interface.Interface)
    grok.view(MyForm)

    def render(self):
        return "BLA BLA BLA"



class LoggedinAs(uvcsite.MenuItem):
    grok.context(interface.Interface)
    grok.viewletmanager(uvcsite.IPersonalPreferences)
    
    @property
    def title(self):
        return "You are logged in as MASTER"




from megrok.z3ctable import TablePage, Column, table

class TableItem(uvcsite.MenuItem):
    grok.context(uvcsite.IMyHomeFolder)
    grok.title("Table")
    action = "title"



class Table(TablePage):
    """
    """
    grok.context(Interface)
    cssClasses = {'table': 'tablesorter'}
    grok.title('Tabelle')
    title = "Tabelle"
    description = "Beispieltabelle"


    startBatchingAt = 10
    batchSize = 10

    @property
    def values(self):
        return range(100)

class Number(Column):
    table(Table)
    grok.context(Interface)
    header = "Number"
    cssClasses = {'td':'right',}

    def renderCell(self, item):
        return item

class SortNumber(Column):
    grok.name('hase')
    table(Table)
    grok.context(Interface)
    header = "SortNumber"

    def renderCell(self, item):
        return item
                   


#
## GroupForm
#


class IPerson(interface.Interface):

    id = schema.TextLine(
       title = u"Id",
       description = u"Id",
       max_length=3,
       )

    name = schema.TextLine(
       title = u"Name",
       description = u"Bitte geben Sie hier den Namen ein",
       )

    vorname = schema.TextLine(
        title = u"Vorname",
        description = u"Bitte geben Sie den Vornamen ein",
        )



class SplitContact(uvcsite.GroupForm):
    grok.title(u'FieldsetBasedForm')
    grok.context(uvcsite.IUVCSite)


class Father(uvcsite.SubForm):
    grok.context(uvcsite.IUVCSite)
    grok.view(SplitContact)
    fields = uvcsite.Fields(IPerson)

    label = "Father"

    @uvcsite.action(u'Abschicken')
    def handleButton(self):
        data, errors = self.extractData()


class Mother(uvcsite.SubForm):
    grok.context(uvcsite.IUVCSite)
    grok.view(SplitContact)
    fields = uvcsite.Fields(IPerson)

    label = "Mother"

    @uvcsite.action(u'Abschicken')
    def handleButton(self):
        data, errors = self.extractData()

