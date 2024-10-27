from django import template

register = template.Library()

@register.filter(name='chunks')
def rows(list_data,row_size):
    row= []
    i=0
    for data in list_data:
        row.append(data)
        i=i+1
        if i==row_size:
            yield row
            i=0
            row=[]
    if row:
        yield row