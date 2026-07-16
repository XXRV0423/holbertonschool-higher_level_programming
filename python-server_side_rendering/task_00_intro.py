#!/usr/bin/python3
import logging

# Configure a basic logger so error messagaes are visible to the user.
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def generate_invitations(template, attendees):
    """"
    Generate personalized invitations files from a template
    and a list of attendees.
    Args:
        template (str): The template string containing placeholders
            such as {name}, {event_title}, {event_date}, and {event_location}.
        attendees (list): A list of dictionaries, each representing
        an attendee with keys matching the template placeholders.
    Return:
        None
    """
    #--- Validate input types ---
    if not isinstance(template, str):
        logger.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees):
        logger.error("Invalid input: attendees must be a list of dictionaries.")
        return

    #--- Handle empty inputs ---
    if template == "":
        logger.error("Template is empty, no output files generated.")
        return
    
    if len(attendees) == 0:
        logger.error("No data provided, no output files generated.")
        return
    
    #--- Process each attendee ---

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            content = content.replace("{" + placeholder + "}", str(value))

        output_filename = "output_{}.txt".format(index)
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(content)
            logger.info("Generated %s", output_filename)
        except IOError as e:
            logger.error("Failed to write %s: %s", output_filename, e)


