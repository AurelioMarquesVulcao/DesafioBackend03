Infoglobo
Desfio Backend Infoglobo
Create a crawler that reads this feed feed https://revistaautoesporte.globo.com/rss/ultimas/feed.xml and return a Json

How to start testing
A test report has been created by simply opening the index.html file in the htmlcov folder.

In the file tests.py was placed 9 unit tests, and the strings, expected for each of the tests.

To repeat the tests just insert new strings.
Were tested:
-The first 4 headlines of the feed.
The first 4 links from feeds.
The first image link from the first article.


Running the tests:

In your terminal open the application folder.
follow the instructions:
coverage run tests.py __ starts the test file.
coverage html __ will create an html report that will be saved in the folder, htmlcov.
