import { client } from "@gradio/client";
import type { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const authHeader = request.headers.get("authorization");
  if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return new Response("Unauthorized", { status: 401 });
  }
  await insertNewReviews();
  return Response.json({ success: true });
}

async function insertNewReviews() {
  const app = await client(
    "https://ryanmiville-fantano-fetcher.hf.space/--replicas/cgsps/",
    {}
  );
  app.predict("/predict", []);
  // wait for 1 second to make sure the request is sent
  await new Promise((resolve) => setTimeout(resolve, 1000));
}
