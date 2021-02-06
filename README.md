# PokeVoter

A bot written in selenium to vote any bots on top.gg.

### Prequisites:
- [Python 3](https://www.python.org)
- [chromedriver](https://chromedriver.chromium.org)


### Get Started:
- Download the correct version of the chromedriver as per your Chrome version 

- Install the selenium module using `pip install selenium` 

- Place it in a folder which is in your environment variables or add the absolute path to the binary to the code using the `executable_path` argument in the `voter.py`

```python
self.driver = webdriver.Chrome() # Executable in path
# OR
self.driver = webdriver.Chrome(executable_path='path/to/chromdriver/binary') # Executable not in path
```
- Open the `config.py` file and enter your discord credentials and the link to the top.gg bot you want to vote for

- Save the file

- Run the `voter.py` file with `python voter.py`



### Notes:
 - If you use another browser look for the required drivers (Firefox is geckodriver , Edge is edge Driver)
 
 - Rest of the details are same except
```python
self.driver = webdriver.Firefox() # Firefox
self.driver = webdriver.Edge() # Microsoft Edge , It might be different I'm not sure
```
 - The binary path instructions are the same
