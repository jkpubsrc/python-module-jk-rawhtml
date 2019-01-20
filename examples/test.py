#!/usr/bin/python3




from jk_rawhtml import *




with HTML5Scope() as H:
	ret = H.html(foo="bar")[
			H.head()[
				H.title[
					"My great web page!"
				]
			],
			H.body(bar="foo")[
				H.a()[
					"A ",
					H.b["great"],
					" web site"
				],
				H.ol[
					H.li[ "Item A" ],
					H.li[ "Item B" ]
				],
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
			H.head()[
				H.raw_style_css(
					"p {",
					"	color: black",
					"}"
				)
			],
			H.body(onload='func_with_esc_args(1, "bar")')[
				H.span(_style="color: black;")[ "Test" ],
				H.span(
					style=CSSMap(
						color="black"
					)
				)[
					"The quick brown fox jumps over the lazy dog."
				],
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
					"This is a test with ",
					H.b[ "bold" ],
					" type face."
				]
			]
		]


print(str(ret))



