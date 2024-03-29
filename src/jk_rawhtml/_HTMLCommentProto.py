

import typing

import jk_prettyprintobj

from .htmlgeneral import *
from .HTMLComment import HTMLComment






class _HTMLCommentProto(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, implClass=HTMLComment):
		self.implClass = implClass
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"implClass",
		]
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __call__(self, *args, **attrs):
		return self.implClass(args)()
	#

	def __getitem__(self, children):
		return self.implClass("".join(children))
	#

#











