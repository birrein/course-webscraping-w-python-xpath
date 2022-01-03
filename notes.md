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
