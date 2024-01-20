import { Review, ReviewsTable } from "@/components/ReviewsTable";

import { db, reviews } from "@/db";

async function selectReviews() {
  return (await db
    .select({
      artist: reviews.artist,
      album: reviews.album,
      rating: reviews.rating,
      publishDate: reviews.publishDate,
    })
    .from(reviews)
    .limit(25)) as Review[];
}

export default async function Home() {
  const data = await selectReviews();
  return (
    <main className="min-h-screen p-24">
      <div className="flex flex-col items-center text-6xl lg:text-8xl font-extrabold pb-4">
        <h1>Fantano</h1>
        <h1>Fetcher</h1>
      </div>
      <section className="max-w-screen-xl mx-auto">
        <ReviewsTable reviews={data} />
      </section>
    </main>
  );
}
