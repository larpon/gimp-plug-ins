#!/usr/bin/env python
# -*- coding: <utf-8> -*-
#
# Quite flexible GIMP python-fu script to export layers.
# It supports all GIMP formats, depends on file save options
#
# Version 1.0
#
# Author: Lars Pontoppidan <leverpostej@gmail.com>
# Copyright (C) 2012 Lars Pontoppidan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from gimpfu import *
import os, re
from os.path import expanduser

def dump(obj):
	print "type: "+type(obj) +"\nattributes: "+ dir(obj)

def dbg(message):
	print message


def export_layers(img, draw, path, visibility, fn, fn_token):

	def traverse(layer,options):
		vis = options['visibility']
		include_layer = (vis == 0 or (vis == 1 and layer.visible) or (vis == 2 and not layer.visible))
		include_group_layer = (vis == 0 or (vis == 1 and layer.visible) or (vis == 2 and not layer.visible))
		if (type(layer) == gimp.GroupLayer):
			if include_group_layer:
				for l in layer.layers:
					traverse(l,options)
		else:
			if include_layer:
				options['keepers'].append(layer)

	layers = []
	options = {
		'visibility' : visibility,
		'keepers' : layers
	}
	for layer in img.layers:
		traverse(layer,options)


	i = 0
	for layer in layers:
		filename = ""
		if fn_token == 1 or fn_token == 2:
			i+=1
			si = str(i)
			if fn_token == 2:
				pad = len(str(len(layers)))
				si = si.zfill(pad)
			filename = re.sub(r'#', si, fn)
		else:
			name = pdb.gimp_item_get_name(layer)
			filename = re.sub(r'#', name, fn)
			
		filename = path+"/"+filename
		dbg("Saving: '"+filename+"'")
		pdb.gimp_file_save(img, layer, filename, filename)
		#interlace, compression, bkgd, gama, offs, phys, time, comment, svtrans = pdb.file_png_get_defaults()
		#pdb.file_png_save2(image, drawable, filename, raw_filename, interlace, compression, bkgd, gama, offs, phys, time, comment, svtrans)

register(
	"export_layers",
	"Export layers",
	"Script to export seperate layers",
	"Lars Pontoppidan",
	"Lars Pontoppidan",
	"2012",
	"E_xport layers...", 
	"*",
	[
		(PF_IMAGE, "img", "Input image", None),
        (PF_DRAWABLE, "draw", "Input drawable", None),
		(PF_DIRNAME, "path", "Output directory", expanduser("~")),
        (PF_OPTION, "visibility", "Visibility", 1, ("All", "Visible", "Invisible")),
        (PF_STRING, "fn", "File pattern", "#.png"),
        (PF_OPTION, "fn_token", "Tokens", 0, ("# = Layer name", "# = Count", "# = Count (zero padded)"))
	],
	[],
	export_layers,
	"<Image>/File/Save/"
)

main() 
