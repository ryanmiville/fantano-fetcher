import { getReviews } from "@/app/api/cron/yt";
import { insert } from "./queries";

async function runSeed() {
  console.log("⏳ Running seed...");
  const start = Date.now();
  const reviews = await (await getReviews()).take(5);
  await insert(reviews);
  const end = Date.now();
  console.log(`✅ Seed completed in ${end - start}ms`);

  process.exit(0);
}

runSeed().catch((err) => {
  console.error("❌ Seed failed");
  console.error(err);
  process.exit(1);
});
