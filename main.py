from durable.lang import ruleset, when_all
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from jinja2 import Environment, FileSystemLoader
import markdown
from durable.lang import *


def generate_html_content(template_path, data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    html_content = template.render(data)
    return html_content


def parse_markdown_to_html(markdown_content):
    parsed_markdown = markdown.markdown(markdown_content)
    return parsed_markdown


def generate_pdf_document(html_content, result_path):
    font_config = FontConfiguration()
    html = HTML(string=html_content)
    html.write_pdf(result_path, font_config=font_config)


def generate_cover_page_data(raw_data):
    result = {
        'exists': False
    }

    with ruleset('cover_page'):
        @when_all(m.exists == True)
        def display_cover_page(c):
            result['exists'] = True
            c.assert_fact({'title': raw_data.get('title') or None})

        @when_all(m.title == None)
        def get_default_title(c):
            result['title'] = 'Default title'
            c.assert_fact({'company_name': raw_data.get('company_name')})

        @when_all(m.title != None)
        def get_customized_title(c):
            result['title'] = c.m.title
            c.assert_fact({'company_name': raw_data.get('company_name')})

        @when_all(m.company_name != None)
        def get_company_name(c):
            result['company_name'] = c.m.company_name
            c.assert_fact({'phone': raw_data.get('phone')})

        @when_all(m.company_name == None)
        def get_company_name(c):
            result['company_name'] = 'Default company'
            c.assert_fact({'phone': raw_data.get('phone')})

        @when_all(m.phone == None)
        def get_default_phone(c):
            result['phone'] = 'Default phone'
            c.assert_fact({'email': raw_data.get('email')})

        @when_all(m.phone != None)
        def get_phone(c):
            result['phone'] = c.m.phone
            c.assert_fact({'email': raw_data.get('email')})

        @when_all(m.email == None)
        def get_default_phone(c):
            result['email'] = 'Default email'

        @when_all(m.email != None)
        def get_phone(c):
            result['phone'] = c.m.email

    assert_fact('cover_page', {'exists': raw_data['exists']})

    return result


def main():
    cover_page = generate_cover_page_data({
        'exists': True,
        'company_name': 'Thanh Dat Amili',
        'title': 'Test customized title'
    })

    with open("./template/markdown_template.md") as f:
        markdown_content = f.read()

    parsed_markdown = parse_markdown_to_html(markdown_content)

    data = {
        "cover_page": cover_page,
        "chapter_page": {
            "highlight": parsed_markdown
        }
    }

    html_content = generate_html_content('./template/book.A4.html', data)
    generate_pdf_document(html_content, './result.pdf')


main()
