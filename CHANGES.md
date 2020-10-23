# Release notes

## 0.0.8

* docs restructured and reintegrated with readthedocs.io
* Fix for a bug in 'expand-columns()' that would cause an error if values were missing/null
* unit tests for v3 historic prices method
* Tidy up usage of "version" across the REST API to make it consistent
* Marked methods that use an outdated version with TODOs
* Fixed issues with switch_account(), delete_working_order() etc. which were not specifying a version correctly
* unit tests for v1, v2 historic prices methods
* allowing historic prices format to be defined at runtime
* new optional flatter format for historic prices
* release notes

## 0.0.7

* CI build fixed
* scheduled integration test added
* initial unit tests created for login, utils
* historical prices methods fixed to use NaN instead of None
* requirements defined explicitly
* fixing flake8 errors
* fixed stream_connection bug
* fixed encrypted password bug
* fixed streaming LOOP problem
* fixed various API version issues
* fixed missing Crypto dependency issue
* fixed Pandas version dependency issue
* support removed for older python versions
* formatting with black
* fixing date format issues
* Fetch multiple client sentiment markets
* PEP8 improvements
* Improve not-found handling on working order creation
* Break out of accounts loop when a user is found
* rest: create_working_order upgrade to v2 api
* Add fetch transaction history v2 api
* Add systemd watchdog support to the lightstreamer library
* Add method to GET current session details
* historical prices v3
* better exception handling
* Update lightstreamer library


## 0.0.6

* initial / undocumented