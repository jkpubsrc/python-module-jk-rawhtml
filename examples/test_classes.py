#!/usr/bin/python3




from jk_rawhtml import *






with HTML5Scope() as H:
	ret = H.html[
			H.head[
				H.title[
					"My great web page!"
				],
			],
			H.body[
				H.div(
					_class=[ "foo", "bar", None, "bar" ],
				)["Lorem ipsum"]
			]
		]

print(str(ret))

