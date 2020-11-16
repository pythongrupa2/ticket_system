#####Ticket System is an private license ticketing and event management application built using the Django Python framework. Ticket System allows event organisers to sell tickets to their events and manage attendees without paying service fees to third party ticketing companies.

*******screen z front_page'u

# Ticket System
Private license ticket selling and event management platform

Please report bugs here: https://github.com/...../issues. 
Detailed bug reports are more likely to be looked at. Simple creating an issue and saying "it doesn't work" is not useful. Providing so me steps to reproduce your problem as well as details about your operating system, Python and Django versions etc can help.

## Django and Python Requirements

asgiref==3.3.0
<br> Django==3.1.2
<br>django-crispy-forms==1.9.2
<br>djangorestframework==3.12.1
<br>Pillow==8.0.1
<br>pytz==2020.1
<br>sqlparse==0.4.1
<br>django-filter==2.4.0
<br>django-phone-field==1.8.1
<br>sqlite version .....

## Current Features (v1.X.X)
tbc
.....

## Contributing

Feel free to fork and contribute. If you are unsure about adding a feature, create a Github issue to ask for Feedback. Read the contribution guidelines

## Submitting an issue

If you encounter a bug in Ticket System, please first search the list of current open Issues on the GitHub repository. You may add additional feedback on an existing bug report. If the issue you're having has not yet been reported, please open a new issue. There is a template available for new issues. Please fill out all information requested in the template so we can help you more easily.

Please note: support is not offered from the project maintainers through GitHub. Paid support is available by purchasing a license.

## Installation

To do a manual installation use the Manual Installation Steps

## Testing
To run the application tests, you can run the following from your project root:

## Troubleshooting
If you are having problems please read the troubleshooting guide

## License
Ticket System is private software licensed. 

## Testing

Before you send your code to remote repository, please run all test locally

<br>$ safety check --full-report
<br>$ black --check -l 120 --exclude=migrations --exclude=venv .
<br>$ flake8 .
<br>$ bandit -x tests,./venv/ -r .
<br>$ isort --check-only --diff .
<br>$ coverage run --omit="venv/*" --branch --source=. ./manage.py test
<br>You can run this commands to fix some bugs from static code analysis:

<br>$ black -l 120 --exclude=migrations --exclude=venv .
<br>$ isort .