# Travel App - Django Project

A full-stack travel booking website built with Django for internship assessment. Users can register, log in, search for travel options (flights, trains, buses), book tickets, and view/manage their bookings.

URL : https://sanchitkumbhar.pythonanywhere.com/
login:- username: root password: 1234

## Features

- User authentication (signup, login, logout, profile update, password change)
- Search and filter travel options by type, source, destination, date, and time
- Book travel tickets and view booking details
- View and manage user bookings (cancel, status)
- Admin panel for managing travel options and bookings
- Responsive UI with Bootstrap

## Project Structure

```
manage.py
requirements.txt
project/
    settings.py
    urls.py
    wsgi.py
    asgi.py
authentication/
    models.py
    views.py
    urls.py
    admin.py
    apps.py
    tests.py
    migrations/
booking/
    models.py
    views.py
    urls.py
    admin.py
    apps.py
    tests.py
    migrations/
traveloptions/
    models.py
    views.py
    urls.py
    admin.py
    apps.py
    tests.py
    migrations/
static/
templates/
    index.html
    home.html
    authentication.html
    profile.html
    travel_options.html
    book_form.html
    user_bookings.html
```

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd project
```

### 2. Install Dependencies

Create a virtual environment and install required packages:

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Database

- MySQL is used. Update `DATABASES` in [`project/settings.py`](project/settings.py) if needed.
- Default credentials:
  - NAME: `traveldb`
  - USER: `root`
  - PASSWORD: `sanchit123`
  - HOST: `localhost`
  - PORT: `3306`

Create the database in MySQL:

```sql
CREATE DATABASE traveldb;
```

### 4. Run Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (for Admin Panel)

```sh
python manage.py createsuperuser
```

### 6. Run the Development Server

```sh
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

## Usage

- **Home Page:** `/`  
  Browse features and search travel options.
- **Authentication:** `/authentication`  
  Register or log in.
- **Travel Options:** `/travel-options`  
  Search and filter available travel options.
- **Book Travel:** `/booking-form/<id>`  
  Book tickets for a selected travel option.
- **My Bookings:** `/client-bookings`  
  View and manage your bookings.
- **Profile:** `/profile`  
  Update profile and change password.
- **Admin Panel:** `/admin/`  
  Manage travel options and bookings.

## Technologies Used

- Django 5.2.5
- MySQL
- Bootstrap 5
- HTML, CSS, JavaScript

## Customization

- Add new travel options via the admin panel.
- Extend models in [`traveloptions/models.py`](traveloptions/models.py) and [`booking/models.py`](booking/models.py) as needed.
- Update templates in [`templates/`](templates/) for UI changes.

## License

This project is for internship assessment and educational purposes.

---

**Author:** Sanchit  
**Year:** 2025
