# Infoglobo
<h1>Infoglobo</h1>
<p> Create a crawler that reads this feed <a>feed https://revistaautoesporte.globo.com/rss/ultimas/feed.xml and return a Json</p>
<h2> How to start testing</h2>
<p>A test report has been created by simply opening the index.html file in the htmlcov folder.</p>

In the file tests.py was placed 9 unit tests, and the strings, expected for each of the tests.

To repeat the tests just insert new strings.<br>
Were tested:<br>
 -The first 4 headlines of the feed.<br>
The first 4 links from feeds.<br>
The first image link from the first article.<br><br>

<h3>Running the tests:</h3><br>
In your terminal open the application folder.<br>
follow the instructions:<br>
coverage run tests.py __ starts the test file.<br>
coverage html __ will create an html report that will be saved in the folder, htmlcov.
