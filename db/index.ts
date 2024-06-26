import { createClient } from "@libsql/client";
import { drizzle } from "drizzle-orm/libsql";
const client = createClient({
  url: process.env.DATABASE_URL as string,
  authToken: process.env.DATABASE_AUTH_TOKEN,
});
export const db = drizzle(client);
export { reviews } from "./schema";
