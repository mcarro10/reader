#!/usr/bin/env python

# configure
TEMPLATE = '/export/reader/etc/tsv2htm-entities.htm'

# require
import sys
import pandas as pd

# sanity check
if len( sys.argv ) != 2 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + "<tsv>\n" )
	quit()

# get input
tsv    = sys.argv[ 1 ]

# slurp up the given file
df = pd.read_csv( tsv, sep='\t' )

rows = ''
for index, row in df.iterrows() :
	
	# parse
	entity    = str( row[ 'entity' ] )
	type      = str( row[ 'type' ] )
	frequency = str( row[ 'frequency' ] )
	
	# build
	rows = rows + "<tr><td>" + entity + "</td><td>" + type + "</td><td>" + frequency + "</td></tr>\n"
	
# slurp up the template and do the substitution
with open( TEMPLATE, 'r' ) as handle : htm = handle.read()
htm = htm.replace( '##ROWS##', rows )

# output and done
print( htm )
exit()