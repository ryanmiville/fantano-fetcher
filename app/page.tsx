import { Review, ReviewsTable } from "@/components/ReviewsTable";

import { getReviews } from "@/db/queries";

export default async function Home() {
  const data = (await getReviews()) as Review[];
  return (
    <main className="min-h-screen p-24">
      <div className="flex flex-col items-center text-6xl font-extrabold pb-4">
        <h1>Fantano Fetcher</h1>
      </div>
      <section className="max-w-screen-xl mx-auto">
        <ReviewsTable reviews={data} />
      </section>
    </main>
  );
}
