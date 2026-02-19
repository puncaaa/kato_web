import zipfile
import xml.etree.ElementTree as ET

docx_path = '/Users/alenpak/Desktop/контент для сайта 2.0/2026 конференци.docx'

try:
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
    
    root = ET.fromstring(xml_content)
    # namespaces in docx xml
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    text = []
    for p in root.findall('.//w:p', ns):
        p_text = ''
        for t in p.findall('.//w:t', ns):
            if t.text:
                p_text += t.text
        if p_text:
            text.append(p_text)
            
    print('\n'.join(text))

except Exception as e:
    print(f"Error: {e}")
