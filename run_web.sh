#!/bin/sh

/usr/bin/gunicorn irongate.wsgi:application -w 2 -b :8000
