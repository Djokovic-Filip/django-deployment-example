from django import template

register = template.Library()

@register.filter(name='cutssd')
def cutssd(value,arg):
    '''
    This cuts out all values of "arg" from the string
    '''
    return value.replace(arg,'')



# register.filter('cut',cut)
