import { NextResponse } from "next/server";

export const runtime = "edge";

export async function GET() {
  const data = {
    "video_id": "RIGINiBYxis",
    "title": "Kendrick Lamar - DAMN. ALBUM REVIEW",
    "artist": "Kendrick Lamar",
    "album": "DAMN.",
    "description":
      "Listen: https:\/\/www.youtube.com\/watch?v=tvTRZJ-4EyI\n\nDAMN. is one of Kendrick's most intriguing releases yet, delivering a series of tracks that are chaotic, layered, and deeply conflicted. \n\nBuy this album: http:\/\/amzn.to\/2oRmsiZ\n\n===================================\nSubscribe: http:\/\/bit.ly\/1pBqGCN\n\nOfficial site: http:\/\/theneedledrop.com\n\nTND Twitter: http:\/\/twitter.com\/theneedledrop\n\nTND Facebook: http:\/\/facebook.com\/theneedledrop\n\nSupport TND: http:\/\/theneedledrop.com\/support\n===================================\n\nFAV TRACKS: HUMBLE, DNA, ELEMENT, LUST, PRIDE, DUCKWORTH, FEAR, XXX, FEEL\n\nLEAST FAV TRACK: LOVE\n\nKENDRICK LAMAR - DAMN. \/ 2017 \/ TOP DAWG ENTERTAINMENT \/ TRAP, POP RAP, CONSCIOUS HIP HOP, WEST COAST HIP HOP\n\n7\/10\n\nY'all know this is just my opinion, right?",
    "thumbnail_url":
      "https:\/\/i.ytimg.com\/vi\/RIGINiBYxis\/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDEgoYcI1Cz8i5Jd0Wyti2v-XdeUw",
    "publish_date": "2017-04-18",
    "watch_url": "https:\/\/youtube.com\/watch?v=RIGINiBYxis",
    "yellow_flannel": true,
    "rating": 7.0,
  };

  return NextResponse.json({ data });
}
