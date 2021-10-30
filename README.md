# nq-cli
### nq-cli is your coding assistant in the terminal. You can create, backup, manage, build, run and add files right from the terminal in no time.

## How to install nq-cli
You can either clone the git repository to your project, or you download the source and unpack the zip file in your project's folder.

## Usage
### Important: nq-cli may overwrite your files in the folder. To make sure nothing can happen, you might install and use nq-cli in an empty folder.

Open the terminal of your operating system. Check your Python installation:

`python3 --version`

Recommended version: higher than `Python 3.6`

Now make sure you are in the correct directory, this means the directory of your project where the "nq-cli" file lays. To start a fullstack project, type:

`python3 nq-cli create fullstack`

nq-cli will now download some source files, install them and build the ground structure of your project. Your project will now contain these things:

- Flask application boilerplate
  - templates folder
    - base.html
    - index.html
    - components folder
      - navbar.html
  - static folder
  - main.py file
- some frameworks
  - bulma.io
  - jQuery

Below is a tree of all nq-cli commands. This list is going to get larger over time as the development of nq-cli proceeds.

- `python3 nq-cli`
  - `create`
    - `fullstack` + optional directory path
  - `run`
    - `fullstack` + optional directory path
  - `build`
    - No templates support builds currently
  - `add`
    - `fullstack`
      - `page` + optional directory path
      - `todo` + optional directory path
      - `text` + optional directory path
    - `license`
      - `mit` + optional directory path
      - `apache` + optional directory path
    - `axome`
      - `auth` + optional directory path
      - `sitemap` + optional directory path
      - `antixsrf` + optional directory path
  - `backup`

To get the command you need, simply follow these elements in the tree.

## Extending nq-cli
Feel free to extend nq-cli, but mind that you are required to deliver the LICENSE file in every distribution.

### How to extend nq-cli
The easiest way to extend nq-cli's functionalty is by copying the fullstack.py file and naming it like your template should be named. Then learn about what the helper functions do:

`_add(filename, content, mode [optional, either w or wb])` adds a file to the current directory

`_switch(directory)` switches to another directory, if it doesn't exist, it creates one

`_leave()` leaves the directory and jumps to `/..`

`i(*info)` logs the progress into the console.

**Every template needs to have the following funtions, because nq-cli is calling them:**

`create(directory)`

Write your code using the helper functions above that create a boilerplate

---

`build(directory)`

Instructions about how to build the application

---

`add(template_name, directory [optional])`

Adds a file template. You do not have to rewrite this function, you can simply change the `template` dictionary.

**Please push your changes to the official nq-cli git repository on github to publish your features. Your name is being added to the CREDITS.md file, your template to the template tree above.**