import random, os, webbrowser, time

# enter url you want to use
url = ""

# change variables to change length of time spent on page in seconds
a = 1
b = 10

# duration is in seconds which is why the range is multiplied by 60
duration = (random.randint(a, b))*60

# boolean for while statement
running = True

# function for the bot behavior
def activateBot():
    webbrowser.open_new(url)
    time.sleep(duration)
    os.system("taskkill /im chrome.exe /f")
    # if you use a different browser change chrome.exe to reflect your browser

# while loop to keep function running
while running:
    activateBot()
