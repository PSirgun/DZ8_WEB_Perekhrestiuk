# coding: utf-8
from models import Author, Quote
import connect
import json

with open('authors.json', 'r', encoding='utf-8') as fa:
    authors_seed = json.load(fa)

for one_author in authors_seed:
    author = Author(
        name=one_author['fullname'],
        born_date=one_author['born_date'],
        born_location=one_author['born_location'],
        description=one_author['description']
    )
    author.save()

with open('quotes.json', 'r', encoding='utf-8') as fq:
    quotes_seed = json.load(fq)

for quote_data in quotes_seed:
    author = Author.objects.filter(name=quote_data['author']).first()

    if not author:
        print ('author not found')
        continue

    quote = Quote(
        quote=quote_data['quote'],
        author=author,
        tags=quote_data['tags']
    )
    quote.save()

print('all ok')