#!/usr/bin/python3




from jk_rawhtml import *




with HTML5Scope() as H:
	ret = H.html(foo="bar")[
			H.head(bar="foo"),
			H.body(bar="foo")[
				H.ul()[
					H.li()[
						"This is a ",
						H.b()["bold"],
						" ",
						H.a(href="https://google.de")[
							"text with > and <"
						],
						"."
					]
				]
			]
		]
	ret = H.html()[
			H.body(onload='func_with_esc_args(1, "bar")')[
				H.div['Escaped chars: ', '< ', u'>', '&'],
				#H.script(type='text/javascript')[
				#	'var lt_not_escaped = (1 < 2);',
				#	'\nvar escaped_cdata_close = "]]>";',
				#	'\nvar unescaped_ampersand = "&";'
				#],
				H.comment(
					"XXX not escaped \"< & >\"",
					"XXX escaped: \"-->\""
				),
				H.comment[
					"YYY not escaped \"< & >\"",
					"YYY escaped: \"-->\""
				],
				H.comment(
					"XXX not escaped \"< & >\"",
					"XXX escaped: \"-->\""
				)[
					"YYY not escaped \"< & >\"",
					"YYY escaped: \"-->\""
				],
				H.div[
					'some encoded unicode: ',
					'你好'
				],
				H.raw_html('<b>My surrounding b tags are not escaped</b>'),
				H.raw_html("The quick ", "brown fox ")["jumps over ", "the lazy dog."],
				H.p(style=CSSMap(margin_left="1px", color=Color.BLUE))[
					"This is a test."
				]
			]
		]



print(str(ret))



