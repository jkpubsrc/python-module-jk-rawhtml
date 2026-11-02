

import jk_logging

import jk_rawhtml




with jk_logging.wrapMain() as log:

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



