# this variable can be used on creating database
export WEB2PY_USE_DB_TESTING="True"
# default port_number
PORT_NUMBER=8020
# remove all temporary in memory files
rm -f /dev/shm/*.table
rm -f /dev/shm/sql.log
rm -f /dev/shm/testing.sqlite
# run web2py
python ../../web2py.py -a 123 -p ${PORT_NUMBER} --no_gui &
# run tests
fades -r requirements.txt -x pytest -v --pdb
# kill web2py
fuser -k -TERM -n tcp ${PORT_NUMBER} > /dev/null
# clear environment variable
unset WEB2PY_USE_DB_TESTING