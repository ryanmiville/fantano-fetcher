import ReviewsTable from "@/components/ReviewsTable";

export default function Home() {
  return (
    <main className="min-h-screen p-24">
      <div className="flex flex-col items-center text-6xl lg:text-8xl font-extrabold pb-4">
        <h1>Fantano</h1>
        <h1>Fetcher</h1>
      </div>
      <section className="max-w-screen-xl mx-auto">
        <ReviewsTable />
      </section>
    </main>
  );
}
