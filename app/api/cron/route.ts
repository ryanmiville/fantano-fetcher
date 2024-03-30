import { insert, mostRecentPublishDate } from "@/db/queries";
import { revalidateTag } from "next/cache";
import type { NextRequest } from "next/server";
import { fmtDate, getReviews } from "./yt";

// export const runtime = "edge";

export async function GET(request: NextRequest) {
  const authHeader = request.headers.get("authorization");
  if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return new Response("Unauthorized", { status: 401 });
  }
  const date = await mostRecentPublishDate();
  const reviews = (await getReviews()).until(
    (review) => fmtDate(review.publishDate) <= date
  );
  const rows = await (await reviews).collect();
  if (!rows || !rows.length) {
    return Response.json({ rows: 0 });
  }
  const affected = await insert(rows);

  revalidateTag("reviews");
  return Response.json({ rows: affected });
}
