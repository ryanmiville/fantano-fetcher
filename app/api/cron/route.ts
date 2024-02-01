import type { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const authHeader = request.headers.get("authorization");
  if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return new Response("Unauthorized", { status: 401 });
  }
  await fireAndForgetUpdateReviews();
  return Response.json({ success: true });
}

async function fireAndForgetUpdateReviews() {
  fetch("https://ryanmiville-fantano-fetcher.hf.space/update", {
    method: "POST",
    cache: "no-store",
  });
  // wait 1 second to make sure the fetch request is sent
  await new Promise((resolve) => setTimeout(resolve, 1000));
}
