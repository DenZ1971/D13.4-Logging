LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'loggers': {
        'django': {
            'handlers': ['general',
                         'console_debug',
                         'console_warning',
                         'console_error',
                         ],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['errors', 'mail_admin'],
            'level': 'DEBUG',
        },
        'django.server': {
            'handlers': ['errors', 'mail_admin'],
            'level': 'DEBUG',
        },
        'django.template': {
            'handlers': ['errors'],
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['errors'],
            'level': 'DEBUG',
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'DEBUG',
        },

    },
    'handlers': {
        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general_formatter',
            'filters': ['require_debug_false'],

        },
        'console_debug': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'debug_formatter',
            'filters': ['require_debug_true'],
        },
        'console_warning': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'warning_formatter',
            'filters': ['require_debug_true'],
        },
        'console_error': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'formatter': 'warning_formatter',
            'filters': ['require_debug_true'],
        },

        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_formatter',

        },
        'security': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'general_formatter',

        },
        'mail_admin': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'warning_formatter',
            'filters': ['require_debug_false'],
        },
    },
    'formatters': {
        'debug_formatter': {
            'format': 'Time: {asctime} Level: {levelname} Message: {message}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',

        },
        'warning_formatter': {
            'format': 'Time: {asctime} Level: {levelname} Message: {message} Path: {pathname}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',

        },
        'error_formatter': {
            'format': 'Time: {asctime} Level: {levelname} Message: {message} Path: {pathname} Stack: {exc_info}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',

        },
        'general_formatter': {
            'format': '{Time: {asctime} Level: {levelname} Module: {module} Message: {message}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',

        },

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },

}
