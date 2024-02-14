import fs from "fs";
import { insert } from "./queries";
import { InsertReview } from "./schema";

async function runSeed() {
  console.log("⏳ Running seed...");
  const start = Date.now();

  const reviews = JSON.parse(
    fs.readFileSync("db/reviews.json", "utf-8")
  ) as InsertReview[];

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
