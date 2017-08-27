languages_lookup = {
             'en': 'English',
             'pl': 'Polski',
             }

def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

def extract_trans(article, lang, url):
  for trans in article.translations:
      if trans.lang == lang:
          return trans.url
  return url

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]