#!/usr/bin/python3




from jk_rawhtml import *






with HTML5Scope() as H:
	ret = H.html[
			H.head()[
				H.title[
					"My great web page!"
				],
				H.style_css[
					CSSStyleGroup("foo", border_left="1px solid black;"),
					CSSStyleGroup("bar"),
					"""foobar {
						border-left: 1px solid black;
						foo: bar;
					}""",
				],
			],
			H.body(bar="foo")[
				H.a()[
					"A ",
					H.b["great"],
					" web site"
				],
				H.ol[
					H.li[ "Item A" ],
					H.li(style=CSSMap(border_color="yellow"))[ "Item B" ],
					H.li(style={
						"border-color": "#ff8000"
					})[ "Item B" ],
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

print(str(ret))

