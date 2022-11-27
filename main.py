from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from year_calc import years_old, validate_form
from collect_data import wines

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


rendered_page = template.render(
    years_old=years_old,
    word_form=validate_form(years_old),
    wines=wines,
)

with open('index.html', 'w', encoding="utf-8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
