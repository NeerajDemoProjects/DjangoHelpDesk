from jinja2 import Environment, Template
env = Environment()

template_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>


</head>
<body>
        {{foo }}
</body>
</html>'''
template = env.from_string(template_code)
context = {'foo': 22}

html_code = template.render(context)


print(html_code)