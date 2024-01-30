import { desc } from "drizzle-orm";
import { cache } from "react";
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

export const getReviews = cache(async () => {
  return await prepared.execute();
});
