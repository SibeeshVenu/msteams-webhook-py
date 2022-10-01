import asyncio
import pymsteams

loop = asyncio.get_event_loop()


def notify_to_teams(message: str, web_hook_url: str, web_hook_name: str):
    '''This function will notify the message in the Teams channel'''
    my_teams_message = pymsteams.async_connectorcard(web_hook_url)
    my_teams_message.title(web_hook_name)
    my_teams_message.text(message)

    # to send the message, pass to the event loop
    loop.run_until_complete(my_teams_message.send())
