from csv import reader
from markdown import markdown
from os.path import exists


def lorem(num_words):
    text = open('Documents/lorem.txt').read()
    return ' '.join(text.split(' ')[:num_words])
    


def card_data(title="Yellow Card", body=lorem(110), color='bg-warning', width='col-lg-12'):
    html = markdown(body)
    return dict(title=title, body=html, color=color, width=width)


def cards_data():
    return [
                card_data(),
                card_data("Green Card",   lorem(40),  "bg-success", 'col-lg-4'),
                card_data("Red Card", lorem(80), "bg-danger", 'col-lg-4'),
                card_data("Blue Card",  lorem(30),  "bg-primary",  'col-lg-4'),
            ]

def markdown_file_data(doc):
    doc = 'Documents/' + doc
    if not exists(doc):
        text = '# 404 is not cool man'
    else:
        text = markdown(open(doc).read())
    title = f'Document - {doc}'
    card = card_data(title, text, 'bg-success', 'col-lg-12') 
    return dict(card=card)

def table_data(path):
    return [row[:5] for row in reader(open(path))]


def tabs_data():

    def options(i, tab, selected):
        if selected:
            return dict(name=f'tab{i}', header=tab['title'], body=tab['body'],
                        active='active', show='show', selected='true')
        else:
            return dict(name=f'tab{i}', header=tab['title'], body=tab['body'],
                        active='', show='', selected='false')
    
    def set_options(tabs):
        return [options(i, tab, i == 2) for i, tab in enumerate(tabs)]
    
    return set_options(cards_data())

def accordion_data():

    def render_card_body(i):
        return f'<h2>Episodes</h2>  <p>Episode {i*5-4}</p><p>Episode {i*5-3}</p><p>Episode {i*5-2}</p><p>Episode {i*5-1}</p><p>Episode {i*5}</p>'

    def card_content(i, active):
        card = dict(id=i, title=f'Season {i+1}', body=render_card_body(i+1))
        if i == active:
            card['show'] = 'show'
            card['active'] = 'true'
        return card

    return [card_content(i, 0) for i in range(6)]