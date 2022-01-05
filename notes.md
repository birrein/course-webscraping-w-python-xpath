## Platzi course: Web scraping with Pythón + XPath

- Tool for test scraping with browser:
http://toscrape.com/

- $x() command in Chrome Dev tools for test xpath, e.g.:

  ```
  $x('//h1/a/text()').map(x => x.wholeText)
  ```

- Operators:
    
    - !=
    - <>
    - and
    - or
    - not

    Operators examples:

    ```    
    $x('//span[@class!="text"]')
    $x('//span[not(@class)]'
    ```

- Xpath cheatsheet: https://devhints.io/

![XPath Cheatsheet](xpath-cheatsheet.webp)

- To create a virtual environment in Python: `python3 -m venv venv`.

- To activate the virtual environment: `source venv/bin/activate`.

- pip freeze: list of installed packages. And with `pip freeze > requirements.txt` we can create te requirements.txt file.

- pip install -r requirements.txt: install the packages in the requirements.txt file.