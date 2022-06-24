import re

def domain_name(url):
    return re.search('(?:www\.)?([\w\d-]+?)\.', url)[1]
