# Secret Sharing Django Application

This Django application allows users to share secrets by generating unique URLs.
When someone opens the URL, they can view the text that was submitted.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (version 3.x)
- Django

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Margarit-Kyurkchyan/secret-sharing.git
```

2. Navigate to the project directory:
```bash
cd secret-sharing-django
```

3. Apply migrations:
```bash
python manage.py migrate
```

4. Start development server:
```bash
python manage.py runserver
```


### Usage
1. Open your browser and go to http://127.0.0.1:8000/.
2. Click on the "Create a secret" button.
3. Enter some text in the input field.
4. Click on the "Create" button.
5. A unique URL will be generated. Share this URL with others.
6. When someone opens the URL, they can view the text you submitted.


### Contributing
Feel free to contribute to the development of this project. Follow these steps:

1. Fork the project.
2. Create your feature branch: git checkout -b feature/your-feature.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature/your-feature.
5. Submit a pull request.

### License
This project is licensed under the MIT License 