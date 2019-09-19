#!/usr/bin/env python3
print("========================================")
print("Website should at http://localhost:5000/")
print("========================================")
print("\n")

from application_folder import flask_instance

flask_instance.run(debug=True)
