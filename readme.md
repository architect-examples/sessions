# Architect sessions example

> A very simple example project for working with Architect JWE and database-backed sessions in JS or Python

This project comes in JavaScript (Node.js) and Python flavors, see: [`js/`](js/) and [`py/`](py/).

In both cases, the instructions for getting started are the same, as found below!


## Getting started

1. `cd` into [`js/`](js/) or [`py/`](py/)
2. Run: `npm install`; if using Python, also be sure to run `pip3 install -r ./requirements.txt`
3. Start the Sandbox: `npm run start`
4. Visit the test app at `http://localhost:3333`


## Things to note

- By default, this app is configured with DynamoDB-backed sessions; the easiest way to test JWE sessions is to comment out the contents of the `.env` file
- This app is deployable! Ship it to AWS to test it live if you like.
- Handler logic is found in `src/http/`:
  - `get /` - contains the basic session setup and web form
  - `get /count` - is a simple session counter incrementer endpoint
  - `get /reset` - is a simple session reset endpoint
