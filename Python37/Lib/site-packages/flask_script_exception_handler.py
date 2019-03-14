__version__ = '0.1.1'


def handle_exception(err, script_logger):
    """Exception handler for processes running under manage.py."""

    from werkzeug.debug.tbtools import get_current_traceback
    traceback = get_current_traceback(ignore_system_exceptions=True)
    script_logger.error('%s\n\n%s' % (err, traceback.plaintext))
