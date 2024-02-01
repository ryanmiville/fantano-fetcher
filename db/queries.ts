import { desc } from "drizzle-orm";
import { unstable_cache } from "next/cache";

import { db, reviews } from ".";

const prepared = db
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

export const getReviews = unstable_cache(
  async () => {
    return await prepared.execute();
  },
  ["reviews"],
  { tags: ["reviews"] }
);
