import grok
from zeam.form.ztk.widgets.choice import RadioFieldWidget, ChoiceSchemaField
from skin import ITBSkin 
from zope.interface import Interface

grok.templatedir('templates')

class UvcRadioFieldWidget(RadioFieldWidget):
    """ Simple Override for removing <br> between choices
    """
    grok.adapts(ChoiceSchemaField, Interface, ITBSkin)

