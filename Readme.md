# LockerProtection

LockerProtection is a web application built using Django, HTML, and CSS and Javascript. It allows users to protect their lockers by setting up personalized access codes.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Installation](#Installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and login
- Locker management
- Dashboard with locker status

## Technologies

- **Frontend:** HTML, CSS, Javascript
- **Backend:** Django
- **Database:** postgresql

## Prerequisites

- Python (3.8 or above)
- Git

## Installation

1. Clone the repository:

   - git clone https://github.com/codequillskills/Locker-Protection

1. Install dependencies:

   - pip install -r requirements.txt

1. Create a virtual environment

   - python -m venv ./env
   - cd env/scripts
   - activate

1. Add the .env file in the root directory as sample provided

1. Set up your database:

   - python manage.py makemigrations
   - python manage.py migrate

1. Create a superuser:

   - python manage.py createsuperuser

1. Run the development server:

   - python manage.py runserver

1. Access the application at `http://localhost:8000/`

## Usage

1. Register an account.
2. Log in and add your lockers.
4. Monitor locker status on the dashboard.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.