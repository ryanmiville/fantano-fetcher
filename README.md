# Fantano Fetcher

Simple Next.js app to fetch and display Anthony Fantano's latest reviews from his YouTube channel.

## Installation

```bash
pnpm install
```

This should allow you to open the project and explore the code. However, you will need to set up a database to run the app, which is probably more trouble than it's worth. 

## Database Setup

This app uses PlanetScale for its database, even in dev mode. If you want to run this app locally, you will need to create a PlanetScale account and a database. Once you have a database, you will need to create a `.env.local` file in the root of the project and add the following environment variables:

```
DATABASE_URL
```

Then you can run `pnpm db:push` to run the necessary migrations to your database.

After your table is created, add the following environment variables to your `.env.local` file:

```
PLANETSCALE_DB_HOST
PLANETSCALE_DB_USERNAME
PLANETSCALE_DB_PASSWORD
```

Even after this, you will want to seed some data. Even though this app fetches data and stores it in the database, it was designed for incremental updates. To seed the database, run the following command:

```bash
pnpm db:seed
```

## Run the app

Now you should finally be able to run the app:

```bash
pnpm dev
```

> Note: I have not tested these instructions. My database is already set up. If you run into any problems, please open an issue and I will try to help you out.