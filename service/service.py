import sys
import ctypes

from cerver import *
from cerver.http import *

from codebox import *

from routes.service import *

codebox_service = None

# end
def end (signum, frame):
	# cerver_stats_print (codebox_service, False, False)
	http_cerver_all_stats_print (http_cerver_get (codebox_service))
	cerver_teardown (codebox_service)
	cerver_end ()

	sys.exit ("Done!")

def codebox_set_service_routes (http_cerver):
	# register top level route
	# GET /api/codebox
	main_route = http_route_create (REQUEST_METHOD_GET, b"api/codebox", main_handler)
	http_cerver_route_register (http_cerver, main_route)

	# GET api/codebox/version
	version_route = http_route_create (REQUEST_METHOD_GET, b"version", version_handler)
	http_route_child_add (main_route, version_route)

def start ():
	global codebox_service
	codebox_service = cerver_create_web (
		b"codebox-service", PORT, CERVER_CONNECTION_QUEUE
	)

	# main configuration
	cerver_set_alias (codebox_service, b"codebox")

	cerver_set_receive_buffer_size (codebox_service, CERVER_RECEIVE_BUFFER_SIZE)
	cerver_set_thpool_n_threads (codebox_service, CERVER_TH_THREADS)
	cerver_set_handler_type (codebox_service, CERVER_HANDLER_TYPE_THREADS)

	cerver_set_reusable_address_flags (codebox_service, True)

	# HTTP configuration
	http_cerver = http_cerver_get (codebox_service)

	codebox_set_service_routes (http_cerver)

	# add a catch all route
	http_cerver_set_catch_all_route (http_cerver, codebox_catch_all_handler)

	# admin
	http_cerver_enable_admin_routes (http_cerver, True)

	# start
	cerver_start (codebox_service)
