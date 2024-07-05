from jinja2 import Template
import os


def generate_report(data):
    template_path = os.path.join(os.path.dirname(__file__), 'template', 'template.html')
    with open(template_path) as f:
        template = Template(f.read())
    report = template.render(data=data)
    with open('report.html', 'w') as f:
        f.write(report)
