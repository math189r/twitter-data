import json

# from twitter
languages = [
  {
    "code": "fr",
    "status": "production",
    "name": "French"
  },
  {
    "code": "en",
    "status": "production",
    "name": "English"
  },
  {
    "code": "ar",
    "status": "production",
    "name": "Arabic"
  },
  {
    "code": "ja",
    "status": "production",
    "name": "Japanese"
  },
  {
    "code": "es",
    "status": "production",
    "name": "Spanish"
  },
  {
    "code": "de",
    "status": "production",
    "name": "German"
  },
  {
    "code": "it",
    "status": "production",
    "name": "Italian"
  },
  {
    "code": "id",
    "status": "production",
    "name": "Indonesian"
  },
  {
    "code": "pt",
    "status": "production",
    "name": "Portuguese"
  },
  {
    "code": "ko",
    "status": "production",
    "name": "Korean"
  },
  {
    "code": "tr",
    "status": "production",
    "name": "Turkish"
  },
  {
    "code": "ru",
    "status": "production",
    "name": "Russian"
  },
  {
    "code": "nl",
    "status": "production",
    "name": "Dutch"
  },
  {
    "code": "fil",
    "status": "production",
    "name": "Filipino"
  },
  {
    "code": "msa",
    "status": "production",
    "name": "Malay"
  },
  {
    "code": "zh-tw",
    "status": "production",
    "name": "Traditional Chinese"
  },
  {
    "code": "zh-cn",
    "status": "production",
    "name": "Simplified Chinese"
  },
  {
    "code": "hi",
    "status": "production",
    "name": "Hindi"
  },
  {
    "code": "no",
    "status": "production",
    "name": "Norwegian"
  },
  {
    "code": "sv",
    "status": "production",
    "name": "Swedish"
  },
  {
    "code": "fi",
    "status": "production",
    "name": "Finnish"
  },
  {
    "code": "da",
    "status": "production",
    "name": "Danish"
  },
  {
    "code": "pl",
    "status": "production",
    "name": "Polish"
  },
  {
    "code": "hu",
    "status": "production",
    "name": "Hungarian"
  },
  {
    "code": "fa",
    "status": "production",
    "name": "Farsi"
  },
  {
    "code": "he",
    "status": "production",
    "name": "Hebrew"
  },
  {
    "code": "ur",
    "status": "production",
    "name": "Urdu"
  },
  {
    "code": "th",
    "status": "production",
    "name": "Thai"
  },
  {
    "code": "en-gb",
    "status": "production",
    "name": "English UK"
  }
]

with open('../example_config.json','r') as f:
    example = json.load(f)
    example.pop('track',None)
    example['stream'] = 'sample'

for lang in languages:
    name = 'config_{}.json'.format(lang['name'].lower().replace(' ','_'))
    example['languages'] = [lang['code']]
    with open(name,'w') as f:
        f.write(json.dumps(example, indent=4, sort_keys=True))
