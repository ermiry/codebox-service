import ctypes

from cerver.http import HTTP_STATUS_OK
from cerver.http import http_response_json_msg_send
from cerver.http import http_response_json_key_value_send

import codebox
import runtime
import version

# GET /api/codebox
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def main_handler (http_receive, request):
	http_response_json_msg_send (
		http_receive,
		HTTP_STATUS_OK,
		b"Codebox Service Works!"
	)

# GET /api/codebox/version
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def version_handler (http_receive, request):
	v = f"{version.CODEBOX_VERSION_NAME} - {version.CODEBOX_VERSION_DATE}"

	http_response_json_key_value_send (
		http_receive,
		HTTP_STATUS_OK,
		b"version", v.encode ("utf-8")
	)

# GET *
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def codebox_catch_all_handler (http_receive, request):
	http_response_json_msg_send (
		http_receive,
		HTTP_STATUS_OK,
		b"Codebox Service Service!"
	)
