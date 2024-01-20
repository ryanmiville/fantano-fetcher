import { connect } from "@planetscale/database";
import { drizzle } from "drizzle-orm/planetscale-serverless";

const connection = connect({
  host: process.env.PLANETSCALE_DB_HOST,
  username: process.env.PLANETSCALE_DB_USERNAME,
  password: process.env.PLANETSCALE_DB_PASSWORD,
});

export const db = drizzle(connection);
export { reviews } from "./schema";
