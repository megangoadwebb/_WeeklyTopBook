User’s Guide:

Welcome to the Weekly Top Books app! This guide will help you set up and run the project to display the New York Times Best Sellers list by genre.


Prerequisites
Before you start, make sure you have the following:
Python 3.x: Ensure that Python is installed on your machine. You can download it from python.org.


API Key: You need a New York Times API key to fetch the best sellers list. Sign up at NY Times Developer Network and obtain your API key.

Setup
Step 1: Clone the Project
Clone the project repository to your local machine. Open your terminal or command prompt and run:

git clone https://github.com/yourusername/nyt-best-sellers.git
cd nyt-best-sellers

Step 2: Install Dependencies
Install the required Python packages using pip. Run the following command in your terminal:

pip install flask requests

Step 3: Create the API_keys.py File
Create a file named API_keys.py in the project directory. Open this file in a text editor and add your New York Times API key and URL as follows:

# API_keys.py
NYT_API_KEY = 'your_nyt_api_key'
NYT_API_URL = 'https://api.nytimes.com/svc/books/v3/lists.json'

Replace 'your_nyt_api_key' with your actual API key.

Running the Project

Step 4: Start the Flask Server
In your terminal, navigate to the project directory and run:

python app.py

You should see output indicating that the Flask server is running, typically on http://127.0.0.1:5000/.

Step 5: Open the Web App
Open your web browser and go to http://127.0.0.1:5000/. You should see the NYT Best Sellers app interface.

Using the Project
Select Genre: Use the dropdown menu to select a genre from the list.
View Best Sellers: The app will display the top books of the week for the selected genre, including the title, author, description, and a link to purchase on Amazon.

Troubleshooting

Common Errors and Fixes
Missing API Key: Ensure that the API_keys.py file exists and contains your NYT API key.


Dependencies Not Installed: Ensure that you have installed all required packages using pip install flask requests.


Server Not Running: If the server fails to start, check the terminal for error messages. Common issues include syntax errors or missing dependencies.

Potential Issues
API Limitations: The New York Times API may have rate limits. If you exceed the limit, you may need to wait before making more requests.


Network Issues: Ensure you have a stable internet connection to fetch data from the NY Times API.

Limitations and Future Enhancements
Detailed Book Profiles: Currently, the app displays basic information. Future updates may include more detailed book profiles.


Error Handling: The app could be improved to handle errors more gracefully and provide better user feedback.


Summary
This guide covers the basic setup and usage of the NYT Best Sellers Project. For more detailed technical information, refer to the developer’s documentation. If you encounter any issues or have suggestions for improvements, feel free to contribute to the project on GitHub. Happy reading!

