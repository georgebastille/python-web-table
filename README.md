# Interactive Web Table UI
The task is to create a web UI for tabluar data, that responds to user supplied queries and displays the results. The drive is that is should be as simple as possible, so far it contains no Javascript (nothing against JS, but if we don't *need* it, lets get rif of it), and is fully contained in 2 files:
* Flask driven webserver
* HTML template

### Why?
Simple is good because it is easy to reason about, easy to debug and easy to modify. Running a query and displaying tables of results is something I do often in code, ususally on the command line. Making this available to others has great value if you want to generate some excitement for your project. Most of my work is in python, so using a python webserver (flask) is a natural fit.
