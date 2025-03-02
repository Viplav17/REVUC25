# DoseWise - Insulin Dosage Calculator

## Getting Started

Follow the steps below to get the DoseWise website up and running on your local machine.

### Step 1: Clone the Repository

If you haven't already cloned the repository, do so by running the following command in your terminal or command prompt:

```bash
git clone https://github.com/your-username/T1D_REVUC.git

Step 2: Open the T1D_REVUC File
Once the repository is cloned, navigate to the folder where the T1D_REVUC file is located. Open this file to start working with the project.

Step 3: Install Django
Before running the server, you'll need to install Django. Open Command Prompt (or your terminal) and run the following command:

bash
Copy
Edit
pip install django
This will install Django on your machine.

Step 4: Run the Server
Next, run the following command to start the Django development server:

bash
Copy
Edit
python manage.py runserver
This will start the server, and you should see output like the following:

pgsql
Copy
Edit
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Step 5: Access the Website
Open your web browser and go to the following URL:

cpp
Copy
Edit
http://127.0.0.1:8000/
You should now see the DoseWise website, where you can calculate insulin dosages based on food intake.

Troubleshooting
If the website doesn't load, ensure that the Django server is still running. You can restart it by running python manage.py runserver again.
If you encounter any errors related to missing dependencies, make sure you have installed all necessary packages and that you're running the correct Python version.
Contributing
Feel free to contribute by submitting a pull request or raising an issue for any bugs or improvements.
