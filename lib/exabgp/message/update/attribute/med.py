# encoding: utf-8
"""
attributes.py

Created by Thomas Mangin on 2009-11-05.
Copyright (c) 2009-2012 Exa Networks. All rights reserved.
"""

from struct import unpack

from exabgp.message.update.attribute import AttributeID,Flag,Attribute

# =================================================================== MED (4)

class MED (Attribute):
	ID = AttributeID.MED
	FLAG = Flag.OPTIONAL
	MULTIPLE = False

	def __init__ (self,med):
		self.med = self._attribute(med)
		self._str = str(unpack('!L',med)[0])

	def pack (self):
		return self.med

	def __len__ (self):
		return 4

	def __str__ (self):
		return self._str
