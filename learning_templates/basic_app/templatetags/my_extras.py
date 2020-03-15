from django import template

register = template.Library()



@register.filter(name='cut')
def cut(value,arg):
    '''
    This cuts out all value of "arg" from the string!
    '''
    return value.replace(arg,'')

#cut = register.filter('cut',cut)
#equal
#register.filter('cut',cut)#
