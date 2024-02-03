import { desc, max } from "drizzle-orm";
import { unstable_cache } from "next/cache";

import { db, reviews } from ".";
import { InsertReview } from "./schema";

const allReviews = db
  .select({
    artist: reviews.artist,
    album: reviews.album,
    rating: reviews.rating,
    publishDate: reviews.publishDate,
    videoId: reviews.videoId,
  })
  .from(reviews)
  .orderBy(desc(reviews.publishDate))
  .prepare();

const maxPublishDate = db
  .select({
    publishDate: max(reviews.publishDate),
  })
  .from(reviews)
  .prepare();

export const getReviews = unstable_cache(
  async () => {
    return await allReviews.execute();
  },
  ["reviews"],
  { tags: ["reviews"] }
);

export async function mostRecentPublishDate() {
  const [{ publishDate }] = await maxPublishDate.execute();
  return publishDate!;
}

export async function insert(rows: InsertReview[]) {
  return (await db.insert(reviews).values(rows)).rowsAffected;
}
