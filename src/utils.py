
import jinja2, pdfkit, datetime, os
def create_pdf(context: dict, path_to_file: str, filename: str):
    if not context:
        raise ValueError('Empty context')
    if not path_to_file:
        raise ValueError('Empty path to file')
    if not filename:
        raise ValueError('Empty filename')
    if not os.path.exists(path_to_file):
        raise FileNotFoundError('Path does not exist')
    
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('template.html')
    output_text = template.render(context)

    path_to_file = f'{path_to_file}{filename}.pdf'
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    pdfkit.from_string(output_text, path_to_file, configuration=config)
    print('PDF created successfully!')

my_name = "John Doe"
item1 = 'TV'
item2 = 'Computer'
item3 = 'Washing Machine'
today_date = datetime.datetime.now().strftime("%Y-%m-%d")


context = {
        'my_name': my_name,
        'item1': item1,
        'item2': item2,
        'item3': item3,
        'today_date': today_date
    }
create_pdf(context=context,template_name='template.html', path_to_file='/home/octavio/Desktop/', filename='invoice')