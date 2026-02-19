#!/bin/bash
python manage.py dumpdata --natural-foreign --natural-primary \
  -e contenttypes -e auth.Permission -e admin.LogEntry \
  --indent 2 > data.json
echo "Data dumped to data.json"
