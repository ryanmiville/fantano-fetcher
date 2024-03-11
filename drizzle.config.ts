import type { Config } from "drizzle-kit";

export default {
  schema: "./db/schema.ts",
  out: "./drizzle",
  driver: "turso",
  dbCredentials: {
    url: process.env.g as string,
    authToken: process.env.DATABASE_AUTH_TOKEN,
  },
} satisfies Config;
