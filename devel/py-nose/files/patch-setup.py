--- setup.py.orig	2015-06-02 08:43:31 UTC
+++ setup.py
@@ -30,7 +30,6 @@ try:
         entry_points = {
         'console_scripts': [
             'nosetests = nose:run_exit',
-            'nosetests%s = nose:run_exit' % py_vers_tag,
             ],
         'distutils.commands': [
             ' nosetests = nose.commands:nosetests',
@@ -106,7 +105,6 @@ setup(
     license = 'GNU LGPL',
     keywords = 'test unittest doctest automatic discovery',
     url = 'http://readthedocs.org/docs/nose/',
-    data_files = [('man/man1', ['nosetests.1'])],
     package_data = {'': ['*.txt',
                          'examples/*.py',
                          'examples/*/*.py']},
