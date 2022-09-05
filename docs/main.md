## CatFish's MAW
This file will (hopefully?) give you a bit of knowledge of what this does and how it
works (in fact, even I don't know).

### Project Structure
`cfmaw/` - contains the source files

`docs/` - the documentation, and has the file you're reading right now

`samples/` - examples of code that demonstrate cfmaw

### Required modules
**I've made this using Python 3.10.2, but I don't know what is the minimum version required.**

`requests` for connecting to the API

`json` for loading the JSON file and printing the various values

### The code itself 
The `__init__` method of each class requires a `server` and `tag` parameter, which is used by
the first two lines of the method, and the third line has the URL that this module connects to.
Whatever you entered into the parameters is then used by `self.url`. The `requests` module is
obviously made to connect to the API, and the `json` module uses the JSON in the URL and can be
stored in the variable `__clan`, `__player`, `__war`, `__token` (depending on the class). Finally,
the different attributes store the values in the JSON, and can be used.

### Using the module
Start by importing the `cfmaw` module, and creating an instance of what you want and its server.
Hashtags are optional.

```
player = cfmaw.Player("S1", "PURU2J0")
print(player.league)
```

Hopefully your output will be something like:

```
Titan1
```

And that's it, replace a few things and you can do a bunch of stuff with it.