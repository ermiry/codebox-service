from cerver.utils import LOG_TYPE_NONE, cerver_log_both

CODEBOX_VERSION = "0.1"
CODEBOX_VERSION_NAME = "Version 0.1"
CODEBOX_VERSION_DATE = "21/10/2021"
CODEBOX_VERSION_TIME = "23:26 CST"
CODEBOX_VERSION_AUTHOR = "Erick Salas"

def codebox_version_print_full ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nCodebox Service Version: %s".encode ("utf-8"),
		CODEBOX_VERSION_NAME.encode ("utf-8")
	)

	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"Release Date & time: %s - %s".encode ("utf-8"),
		CODEBOX_VERSION_DATE.encode ("utf-8"),
		CODEBOX_VERSION_TIME.encode ("utf-8")
	)

	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"Author: %s\n".encode ("utf-8"),
		CODEBOX_VERSION_AUTHOR.encode ("utf-8")
	)

def codebox_version_print_version_id ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nCodebox Service Version ID: %s\n".encode ("utf-8"),
		CODEBOX_VERSION.encode ("utf-8")
	)

def codebox_version_print_version_name ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nCodebox Service Version: %s\n".encode ("utf-8"),
		CODEBOX_VERSION_NAME.encode ("utf-8")
	)
