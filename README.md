# Assignment

## Steps to setup the backend:
- cd into the folder containing the backend source code
- Make sure that Anaconda or Miniconda is installed in your system. The files manage.py and environment.yaml should be in those particular directories. 
- Run command 'conda env create -f environment.yaml'.
- Then run 'conda activate env_blood_donor'
- Then run 'python manage.py runserver 0.0.0.0:8000 --insecure'. This will start the server and the webapp will be served over port 8000.
- Note that all the other credentials such as to connect to the database is present in blood_donor/credentials.py.


## Steps to setup the frontend:
- cd into the folder containing the front end source code. The file package.json should be present in that directory.
- Make sure npm is installed in your system. Make sure vue cli is installed in your system.
- Run 'rm -rf node_modules'. Sometimes it's beneficial to remove the node modules folder and reinstall the dependencies.
- To reinstall the dependencies, run 'npm install'
- To run the development server, run 'npm run serve'.
- To generate files for dist, run 'npm run build'.
- cd into the dist folder and to serve it, run 'python -m http.server 8080'. The frontend can then be served over port 8080.

## Steps to access the database directly:
- Make sure you have pgAdmin 4 installed on your system.
- open <backend_base_folder>/blood_donor/credentials.py and find the necessary credentials to access the database.

## Extra notes regarding the hosted server:
- The backend is hosted in development mode using the command 'python manage.py runserver 0.0.0.0:8000 --insecure'. This is served over port 8000.
- The frontend is hosted after generating dist folder using the command 'python -m http.server 8080'. This is served over port 8080.
- Both the front end and backend process is running inside tmux in detached mode.

## Access the webapp
- To access the webapp, open your favorite browser and go to http://blooddonorbackend.ddns.net:8080.

