#!/bin/sh
. ~/.bash_profile
spark-submit \
--master local \
--py-files dist/guidedcapstone-1.0-py3.7.egg \
--jars jars/postgresql-42.2.14.jar \
source/run_reporter.py \
config/config.ini
