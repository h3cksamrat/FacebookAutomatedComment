from FacebookAutoComment import Browser, FacebookCommenting
from time import sleep
from getpass import getpass


def my_intro():
    print("             Automation of facebook comment by h3ck(Samrat).",
          end="\n\n")


if __name__ == "__main__":

    try:
        my_intro()

        previousSetsOfTabs = set()
        setOfCommentTabs = set()
        currentSet = set()

        email = input("Email: ")
        password = getpass()
        print("Logging in...")

        browser = Browser().openChrome()
        facebook = FacebookCommenting(browser, email, password)

        facebook.openFacebook()
        facebook.login()
        sleep(6)

        desiredComment = (input(
            "\nEnter the comment you want to be automated (default: #StopVoilenceOnHuman): "
        ) or "#StopVoilenceOnHuman")

        desiredPage = input(
            "Enter url of the desire page you want to comment on (default : On your facebook homepage)\n Example : https://www.facebook.com/username/ \n==> "
        )

        if desiredPage != "\n":
            facebook.switchPage(desiredPage)
            sleep(5)

        print("Opened page...")
        print("To end press Ctrl + C")

        commentTabs = facebook.selectComment()

        setOfCommentTabs = set(commentTabs)
        currentSet = setOfCommentTabs.difference(previousSetsOfTabs)
        previousSetsOfTabs.update(currentSet)

        facebook.comment(currentSet, desiredComment)

        SCROLL_PAUSE_TIME = 5

        last_height = browser.execute_script(
            "return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

            commentTabs = facebook.selectComment()

            #updating the database in set
            setOfCommentTabs = set(commentTabs)
            currentSet = setOfCommentTabs.difference(previousSetsOfTabs)

            facebook.comment(currentSet, desiredComment)

            #updates the used post to comment
            previousSetsOfTabs.update(currentSet)
    except KeyboardInterrupt:
        print('Caught KeyboardInterrupt')
        browser.quit()
