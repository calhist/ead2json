# ArchivesSpace EAD XML to JSON
# A script to parse EAD XML and write out to JSON, which can then be imported to OpenRefine
# by Bill Levay for California Historical Society

import codecs, json, lxml.etree as ET

filepath = 'source.xml'
ead_data = []
ns = '{urn:isbn:1-931666-22-9}'

tree = ET.iterparse(filepath, events=('end', ))

for event, elem in tree:
	
	items = elem.findall(ns+'c02')
	
	for item in items:

		meta = {}

		# get folder title from the c01 parent element
		folder_title = item.getparent().find('.//'+ns+'did/'+ns+'unittitle')
		if folder_title is not None:
			meta['folder title'] = folder_title.text
		
		# get item metadata
		box = item.find('.//'+ns+'container[@type="Box"]')
		if box is not None:
			meta['box'] = box.text
		
		folder = item.find('.//'+ns+'container[@type="Folder"]')
		if folder is not None:
			meta['folder'] = folder.text
		
		title = item.find('.//'+ns+'unittitle')
		if title is not None:
			meta['title'] = title.text

		date = item.find('.//'+ns+'unitdate')
		if date is not None:
			meta['date'] = date.text

		gen_note = item.find('.//'+ns+'odd/'+ns+'p')
		if gen_note is not None:
			meta['general note'] = gen_note.text

		scope_note = item.find('.//'+ns+'scopecontent/'+ns+'p')
		if scope_note is not None:
			meta['scope note'] = scope_note.text

		if len(meta) > 0:
			ead_data.append(meta)

# write out to json
with codecs.open('data.json', 'w', encoding='UTF-8') as json_out:

    # write the list of dictionaries to json
    dump = json.dumps(ead_data, sort_keys=True, indent=4)
    json_out.write(dump)

# close the file
json_out.close

print "All done! Your JSON file is ready."