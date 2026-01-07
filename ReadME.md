# CS 406 API
This is a simple API built using flask as an interface for Google Cloud Datastore. It is designed to support a react front end for budgeting tasks.

## Dependencies
- Python 3.x
- Flask
- google-cloud-datastore
- requests

## Setting up the Environment
This project requires use of a Google Cloud account and the Google Cloud cli. More information on setting up the Google Cloud cli can be found [here](https://cloud.google.com/sdk/docs/install).

## Installation and Startup Instructions
Create a virtual environment and install the relevant dependencies using:
`pip install -r requirements.txt`

To run the application, use:
`python app.py`

## Notes
This application will use port 8080 for the local API server. The front end runs on port 3000, the default port for Vite React applications.

### Front End
The front end code can be found in the following repository: [CS 406 Front End](https://github.com/pdxgrantc/cs406-frontend)

### Testing
I have built a postman environment to test the API endpoints. The configuration files for which can be found in the `postman` directory. These tests are not exhaustive nor are they fully automated but they should return the correct responses and response codes for each endpoint.
