from lettuce import before, world, after
from splinter import Browser
from django.core.management import call_command

@before.all
def set_up_browser():
    world.browser = Browser()
    
@before.each_scenario
def flush_database(step):
    call_command('flush', interactive=False)

@after.all
def close_browser(total):
    world.browser.quit()