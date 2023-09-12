from setuptools import setup, find_packages

setup(
    name="ml_insights",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'blinker==1.6.2',
        'click==8.1.7',
        'Flask==2.3.3',
        'Flask-SQLAlchemy==3.0.5',
        'greenlet==2.0.2',
        'iniconfig==2.0.0',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.3',
        'packaging==23.1',
        'pluggy==1.3.0',
        'psycopg2==2.9.7',
        'pytest==7.4.2',
        'python-dotenv==1.0.0',
        'SQLAlchemy==2.0.20',
        'typing_extensions==4.7.1',
        'Werkzeug==2.3.7'
    ],
    entry_points={
        'console_scripts': [
            # If you want to make command-line scripts available:
            # 'script-name = yourproject.module:function'
            'script-name = ml_insights.app.app:main'
        ]
    },
    author="Morgann Thain",
    description="Instalily new ml-service: Creates and updates a database in a Python Flask application with Pandas to store ML tagging data for media from native-pipeline",
    # license="GNU AGPLv3",
    url="https://github.com/Instalily/ml_insights",
)
