import urllib.request,json
from .models import Quote


# # Getting the movie base url
# base_url = None


# def configure_request(app):
#     global base_url
#     base_url = app.config['QUOTE_API_BASE_URL']

def get_quote():
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)
        quote_object = None
        if quote_details_response:
            author = quote_details_response.get('author')
            quote = quote_details_response.get('quote')
            quote_object = Quote(author, quote)
    return quote_object        