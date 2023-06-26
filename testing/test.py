#!/usr/bin/python3




import jk_rawhtml
import jk_hwriter




with jk_rawhtml.HTML5Scope() as H:
	ret = H.html()[
			H.body(onload='func_with_esc_args(1, "bar")')[
				H.div[
					'Escaped chars: ', '< ', u'>', '&'
				],
				H.div[
					"foo < & > bar",
				],
				H.raw_html('<b>My surrounding b tags are not escaped</b>'),
			]
		]


print(str(ret))



