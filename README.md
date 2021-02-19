# MAIA Blocks Instagram Bot
MAIA Blocks is a serie of intelligent models to help users to build automated audience on Instagram.

* This script is compatible with Windows, MacOS and Linux. 
* Make sure you have the compatible webdriver for your OS (find out more about chrome webdrivers in the link: https://chromedriver.chromium.org/downloads)

The script uses Selenium to perform, make sure you have installed.

$shell: pip install selenium

Important: Make sure your download chromewebdriver.exe and _data.db in order to make the script work properly. Keep all files in the same folder.

# doengagement.py

When the script is executed, it will ask for the following parameters:
1. Username -> Your Instagram Username
2. Password -> Your Instagram Password
3. Hashtag -> Hashtag target to perform engagements
4. Limit -> Limit amout of engagements to be performed by the script before the function is complete.

The script will perform engagements with posts related to the Hashtag provided and scrape informations about the post engaged. These are the data being collected by the script.
1. Instagram handle
2. Post URL
3. Date and Time of the engagement

The script will ralate the data collected to your Instagram handle and the target Hashtag. All data are stored in _data.db.

note: This version will work properly only in computers using English as default language, as it uses plain language to locate and interact with SVG elements. Be free to make the needed language changes and update the repository with your version.

On line 80: driver.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"]').click()

Like has to be replaced to the corresponding language of your OS. (Instagram loads the language based in your OS settings)

# _data.db

The script uses SQLite3 as Database to store data from engaged posts, you may consider using DB Browser for SQLite3 in order to read the data collected.
All data collected is important for the futher functions that I am incrementing in the bot.

Get DB Browser: https://sqlitebrowser.org/

# chromewebdriver.exe

Highly needed for the script to work. Make sure you have the right version compatible with your OS and version of Google Chrome.

# doexplorer.py

In development

# dostalk.py

In development

# sharepost.py

In development

# sharemessage.py

In development

* If you have any doubts about how to use the Script, feel free to reach me out on Instagram - https://www.instagram.com/wellyington
