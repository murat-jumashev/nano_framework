from jinja2 import Template

def render(file_name, context=None):
    with open(file_name, 'r') as html_file:
        html = html_file.read()
        if context:
            template = Template(html)
            # context может быть таким: {'some_var':'some_value'}
            html = template.render(context)
        return html


