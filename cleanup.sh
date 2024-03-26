
mv "`pwd`/openrouteservice/utility.py" "`pwd`/utility.py"

rm -r docs
rm -r .tox
rm -r openrouteservice
rm -r openrouteservice.egg-info
rm README.md
rm setup.py
rm requirements.txt
rm test-requirements.txt
rm tox.ini
rm .travis.yml
rm git_push.sh

mkdir openrouteservice
mv "`pwd`/utility.py" "`pwd`/openrouteservice/utility.py"

mkdir test/bup
mv test/test_*_api.py test/bup/
rm test/test_*.py
mv test/bup/* test/
rmdir test/bup/
