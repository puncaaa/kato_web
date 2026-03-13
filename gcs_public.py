import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/alenpak/Desktop/kato/migration_data/secret.json'

try:
    client = storage.Client()
    bucket = client.bucket('kato-web')
    blob = bucket.blob('events/new_sliderconf.jpeg')
    blob.make_public()
    print('SUCCESS: Image is now public:', blob.public_url)
    
    blob2 = bucket.blob('events/programs/anons_2026.pdf')
    blob2.make_public()
    print('SUCCESS: PDF is now public:', blob2.public_url)
except Exception as e:
    print('ERROR:', e)
