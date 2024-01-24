import { desc } from "drizzle-orm";
import { cache } from "react";
import { db, reviews } from ".";

export const getReviews = cache(async () => {
  return await db.select().from(reviews).orderBy(desc(reviews.publishDate));
});
