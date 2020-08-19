from FacebookAutoComment import Browser, FacebookCommenting
from time import sleep
from getpass import getpass


def my_intro():
    print("             Automation of facebook comment by h3ck(Samrat).",
          end="\n\n")
    print(
        "You are the one responsible for any of your act using this piece of software."
    )

    print("     -h3ck from h3ck Ph4se", end="\n\n")


if __name__ == "__main__":

    try:
        #myIntro
        my_intro()

        #initialization of variables
        previousSetsOfTabs = set()
        setOfCommentTabs = set()
        currentSet = set()

        #password and email input
        email = input("Email: ")
        password = getpass()
        print("Logging in...")

        #object creation
        browser = Browser().openChrome()
        facebook = FacebookCommenting(browser, email, password)

        #method calling
        facebook.openFacebook()
        facebook.login()
        sleep(6)

        #desired comment and desired page for comment
        desiredComment = (input(
            "\nEnter the comment you want to be automated (default: #JusticeForNirmalaPanta): "
        ) or "#JusticeForNirmalaPanta")

        desiredPage = input(
            "Enter url of the desire page you want to comment on (default : On your facebook homepage)\n Example : https://www.facebook.com/UMLprezKPSharmaOli/ \n==> "
        )

        if desiredPage != "\n":
            facebook.switchPage(desiredPage)
            sleep(5)

        print("Opened page...")
        print("To end press Ctrl + C")

        #first selection of commentElemnts
        commentTabs = facebook.selectComment()

        #this is to not to repeat the comment on the same post
        setOfCommentTabs = set(commentTabs)
        currentSet = setOfCommentTabs.difference(previousSetsOfTabs)
        previousSetsOfTabs.update(currentSet)

        #makes the comment
        facebook.comment(currentSet, desiredComment)

        #time for scroll to pause
        SCROLL_PAUSE_TIME = 5

        # Get scroll height
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

            #comment on every post
            commentTabs = facebook.selectComment()

            #updating the database in set
            setOfCommentTabs = set(commentTabs)
            currentSet = setOfCommentTabs.difference(previousSetsOfTabs)

            #makes the comment
            facebook.comment(currentSet, desiredComment)

            #updates the used post to comment
            previousSetsOfTabs.update(currentSet)
    except KeyboardInterrupt:
        print('Caught KeyboardInterrupt')
        browser.quit()
