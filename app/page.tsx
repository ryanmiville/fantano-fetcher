import { getReviews } from "@/db/queries";
import { ReviewColumn, columns } from "../components/columns";
import { DataTable } from "../components/data-table";
import { MainNav } from "../components/nav-bar";

export default async function Home() {
  const data = (await getReviews()) as ReviewColumn[];
  return (
    <main className="min-h-screen">
      <MainNav />
      <div className="p-24">
        <section className="max-w-screen-xl mx-auto pt-16">
          <DataTable data={data} columns={columns} />
        </section>
      </div>
    </main>
  );
}
