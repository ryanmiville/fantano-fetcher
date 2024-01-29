import { getReviews } from "@/db/queries";
import { ReviewColumn, columns } from "../components/columns";
import { DataTable } from "../components/data-table";
import { MainNav } from "../components/nav-bar";

export default async function Home() {
  const data = (await getReviews()) as ReviewColumn[];
  return (
    <main className="min-h-screen">
      <MainNav />
      <div className="px-8 max-w-screen-xl mx-auto flex flex-col justify-center h-[calc(100vh-96px)]">
        <div>
          <DataTable data={data} columns={columns} />
        </div>
      </div>
    </main>
  );
}
