import type { NextRequest } from "next/server";
import { unstable_useCacheRefresh } from "react";

export const runtime = "edge";

const refreshCache = unstable_useCacheRefresh();

export async function GET(request: NextRequest) {
  const authHeader = request.headers.get("authorization");
  if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return new Response("Unauthorized", { status: 401 });
  }

  const resp = await fetch(
    "https://ryanmiville-fantano-fetcher.hf.space/update",
    {
      method: "POST",
      cache: "no-store",
    }
  );
  if (!resp.ok) {
    return new Response("Failed to update data", {
      status: resp.status,
    });
  }

  refreshCache();
  return Response.json({ success: true });
}
