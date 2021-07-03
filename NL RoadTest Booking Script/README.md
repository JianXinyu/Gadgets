## Environment 

- Ubuntu 18.04
- Firefox
- Python 3.6.9
- Python package: selenium, playsound

## Usage

- download all files into a single directory
- set your information and your desired test city in `appointment.py`
- run `appointment.py`

## Troubleshooting

1. Exception has occurred: ElementNotInteractableException Message: Element <option> could not be scrolled into view

   You have to scroll down the webpage to display the desired elements on the screen. 

   Use method `location_once_scrolled_into_view`, e.g., `calender.location_once_scrolled_into_view`