import { ReviewColumn, columns } from "@/components/columns";
import { DataTable } from "@/components/data-table";
import { MainNav } from "@/components/nav-bar";
import { getReviews } from "@/db/queries";

export const revalidate = 43200;

export default async function Home() {
  const data = (await getReviews()) as ReviewColumn[];
  return (
    <main className="min-h-screen">
      <MainNav />
      <div className="px-8 pt-20 max-w-screen-xl mx-auto">
        <div>
          <DataTable data={data} columns={columns} />
        </div>
      </div>
    </main>
  );
}
