
**Inventory Management System**

  

A simple Django web application for managing and tracking equipment assigned to employees within an organization.

  

**Features**

  

•  **Admins can:**

•  Add employees and equipment.

•  Assign equipment to employees.

•  Manage assignments.

•  **Employees can:**

•  View the equipment assigned to them.

  

**Installation**

  

1. **Clone the repository:**

    git clone https://github.com/stokry/inventory-app.git
    cd inventory-management-system

**Create a virtual environment:**

    python -m venv venv

3. **Activate the virtual environment:**

•  On Windows:

    venv\Scripts\activate

On macOS/Linux:

    source venv/bin/activate

4. **Install dependencies:**

    pip install -r requirements.txt


**Set up environment variables:**

•  Create a .env file in the project root directory.

•  Add the following variables:

    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

Replace your-secret-key with a unique, secure key.

**Apply migrations:**

    python manage.py migrate


**Create a superuser (optional):**

    python manage.py createsuperuser

**Collect static files:**

    python manage.py collectstatic


**Run the development server:**

    python manage.py runserver
