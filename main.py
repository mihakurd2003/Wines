from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse
from year_calc import years_old, get_number_end
from collect_wines import process_wines


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Путь до вашего файла', default='wines.xlsx')
    args = parser.parse_args()

    rendered_page = template.render(
        years_old=years_old,
        word_form=get_number_end(years_old),
        drinks=process_wines(args.path),
    )

    with open('index.html', 'w', encoding="utf-8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
