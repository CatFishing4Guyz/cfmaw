## CatFish's MAW
This random file will (hopefully?) give you a bit of knowledge of what this module does and how it works (in fact, even I don't know).

### Project Structure
`cfmaw/` - contains the source files

`docs/` - the documentation, and has the file you're reading right now

`README.md` - the README file

### Required modules
**I've made this using Python 3.10.2, but I don't know what is the minimum version required.**

`requests` for connecting to the API

`json` for loading the JSON file and printing the various values

**Note: Both modules already exist when you install Python**

### The code itself
Each file (except `__init__.py`) has a class with the same name as the file. 
The `__init__` method requires a `tag` parameter, which is used by the first line of the method, and the second line has the url that this module connects to.
Whatever you entered into the tag parameter is then used by `self.url`.
Other objects will then use the `requests` module to make a request, and the `json` module uses the JSON in the url and is stored in the variable `jsonInfo`.
Then a variable is made which uses `jsonInfo` and gets a particular value in the JSON, which is then returned.
This is then repeated for everything in the JSON I consider relevant.

### Using the module
Start by importing the `cfmaw` module, and creating an instance of what you want and its server.

***Note: A hashtag will result in an error***
```
tag = input("Enter a tag: ")
playerS1 = cfmaw.PlayerS1(tag)
print(playerS1.league())
```

Hopefully your output will be something like:
```
Legendary
```

And that's it, replace a few names and you can do a bunch of stuff with this module.
