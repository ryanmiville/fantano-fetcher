# Fantano Fetcher

Simple Next.js app to fetch and display Anthony Fantano's latest reviews from his YouTube channel.

## Installation

```bash
pnpm install
```

This should allow you to open the project and explore the code. However, you will need to set up a database to run the app, which is probably more trouble than it's worth. 

## Database Setup

This app uses Turso for its database, making it seemless to use a simple SQLite file for local dev. 

Ensure you have a `.env.local` file in the root of the project with the following environment variable:

```
DATABASE_URL='file:fantano.db'
```

> Note: fantano.db is not kept up to date, but it does have plenty of data for development purposes
.
## Run the app

Now you should be able to run the app:

```bash
pnpm dev
```