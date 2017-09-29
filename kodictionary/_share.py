def download(dictionary_name):
    import requests
    url_base = 'https://raw.github.com/lovit/sharing_korean_dictionary/master/kodictionary/{}'
    url = url_base.format(dictionary_name)
    r = requests.get(url)
    text = r.text if r.text else ''
    return text

def dictionary_list():
    import os
    directory = '/'.join(os.path.abspath(__file__).replace('\\', '/').split('/')[:-1])
    meta_fname = '{}/meta.json'.format(directory)
    import json
    with open(meta_fname, encoding='utf-8') as f:
        dicts = json.load(f)
    return dicts