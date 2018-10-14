This is a collection of my attempts at solving problems from the codility website.

## Installation

```bash
$ git clone git@github.com:ardenn/codility.git
$ cd codility
$ pip install -r requirements.txt
```

### Requirements
* Python 3
* pytest


## Structure

The questions are found under the `questions` subdirectory, inside text files.
These text files have a structure of `lesson{lesson_number}_{lesson_name}`.
The question files contain a complete description of the problem, examples of expected outcomes, instructions as well as constraints within which to work by.

Solutions can be found under the `solutions/` directory presented as individual modules that define a `solution` function, for each of the questions. For clarity, the file names for the solutions are similar to their question file names.

I have written unit tests under the `tests/` directory, with a single module for each of the questions. Again for clarity, test file names are just the problem/solution file names prefixed with "test_" to allow pytest to discover tests.


## Contributing
Pull requests are welcome. Please feel free to correct me on where I might have gone wrong or even insight in to how some things could have been improved.
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)