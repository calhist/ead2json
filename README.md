# ead2json
A script to parse ArchivesSpace EAD XML and write out to JSON.

## Why did we need this?

At CHS some image collections that are digitized and ingested into Islandora were first cataloged in ArchivesSpace with basic metadata, and an EAD finding aid was generated and submitted to [OAC](http://www.oac.cdlib.org/institutions/California+Historical+Society).

We can reuse that metadata as the starting point for the creation of more robust MODS records. But first we'll have to get it out of the EAD XML and into a spreadsheet or OpenRefine.

This script will help you do just that. As is, it's highly tailored to the ArchivesSpace EAD output, so you may need to rework the parts of this script that find specific values in the XML.

You'll end up with a JSON file that can be directly imported to OpenRefine, where you can do all sorts of metadata magic.

## Running the script

The script is expecting your EAD XML to be called **source.xml** and live in the same directory as the script. But you can change the value of the filepath in line 7:

    filepath = 'source.xml'

Next, you'll probably need to change the **namespace** value in line 9, since that will probably be specific to your EAD. This is the value in curly brackets that is prepended to every element when the XML is parsed. For the collection we recently processed, it looked like this:

    ns = '{urn:isbn:1-931666-22-9}'

Then, depending on how your EAD is structured and what metadata it contains, you may need to change or make additions to the metadata that's collected in the for loop, roughly lines 21-52.

Good luck!
