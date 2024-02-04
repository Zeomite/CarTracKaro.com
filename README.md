

# CarTracKaro.com
Currently hosted at [CarTracKaro.com](https://car-track-karo.vercel.app)

CarTracKaro.com is a Python project that utilizes the `firebase_admin` and `flask` libraries to create a car tracking application. The purpose of this application is to track the location of cars using real-time data and display it on a web interface.

## Prerequisites

Before running the CarTracKaro.com project, make sure you have the following prerequisites installed:

- Python 3.9: [Download Python](https://www.python.org/downloads/)
- `firebase_admin` library: Install using `pip install firebase_admin`
- `flask` library: Install using `pip install flask`

## Installation

1. Clone the repository using the following command:

   ```bash
   git clone https://github.com/Zeomite/CarTracKaro.com.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CarTracKaro.com
   ```

3. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

4. Rename `config_example.py` to `config.py` and update it with your Firebase project credentials.

## Usage

To run the CarTracKaro.com project, follow these steps:

1. Run the `main.py` file:

   ```bash
   python main.py
   ```

2. The application will start running on `http://localhost:5000`. Open this URL in your web browser.

3. Use the web interface to track the location of cars.

## Configuration

In order to connect to your Firebase project, make sure to update the `config.py` file with the appropriate credentials. This file should be placed in the root directory of the project.

Here's an example of the `config.py` file structure:

```python
# config.py

config = {
    'apiKey': 'YOUR_API_KEY',
    'authDomain': 'YOUR_PROJECT_ID.firebaseapp.com',
    'databaseURL': 'https://YOUR_PROJECT_ID.firebaseio.com',
    'projectId': 'YOUR_PROJECT_ID',
    'storageBucket': 'YOUR_PROJECT_ID.appspot.com',
    'messagingSenderId': 'YOUR_MESSAGING_SENDER_ID',
    'appId': 'YOUR_APP_ID',
    'measurementId': 'YOUR_MEASUREMENT_ID'
}
```

Make sure to replace the placeholder values with your actual Firebase project credentials.



## Contact

If you have any questions or suggestions, please feel free to contact the project maintainer at varunusar@gmail.com.

---

Happy tracking with CarTracKaro.com!
