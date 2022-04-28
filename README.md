## CatFish's MAW
API Wrapper for Clash of Magic, named after the 5th dungeon in Link's Awakening (one of my favorite games), written in Python.

**Note: This is not an official thingy**

Visit the API here: https://api.clashofmagic.cc

There is also another wrapper written in TypeScript by Jelosus2 which you can find [here](https://github.com/Jelosus2/clashofmagic.js).

But mine is obviously better ;)

## Documentation
You can find it [here](https://github.com/Monkeys30/cfmaw/tree/main/docs/main.md).

There isn't much there at the moment. When I learn JavaScript or something I'll maybe build a website.

## Installing
```
git clone https://github.com/Monkeys30/cfmaw
cd cfmaw
python setup.py install
```

## Some stuff to keep in mind
* Installing does not work, just do what [#2](https://github.com/Monkeys30/cfmaw/issues/2) suggests.

* For Discord bots, using this wrapper for a slash command will not work.
	* All it's going to do is return `Unknown Interaction`, which happens when the bot takes too long (more than 3 seconds) to respond.

## Credits
Magic Man, for developing the API, a bunch of help, and pointing out stupid mistakes.
