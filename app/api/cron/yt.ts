import { InsertReview } from "@/db/schema";
import { google, youtube_v3 } from "googleapis";

const playlistId = "UUt7fwAhXDy3oNFTAzF2o8Pw";

// Initialize the YouTube API client
const youtube = google.youtube({
  version: "v3",
  auth: process.env.YOUTUBE_API_KEY,
});

export const fmtDate = (date: string) =>
  new Date(date).toISOString().split("T")[0];

export async function getReviews() {
  const reviews = getPlaylistVideosGenerator(playlistId);
  return new Reviews(reviews);
}

async function* getPlaylistVideosGenerator(playlistId: string) {
  let pageToken = "";
  do {
    const response = await youtube.playlistItems.list({
      playlistId: playlistId,
      maxResults: 5,
      part: ["snippet"],
      pageToken,
    });
    pageToken = response.data.nextPageToken as string;
    const items = response.data.items || [];
    const albumReviews = items.filter((item) =>
      item.snippet?.title?.endsWith("ALBUM REVIEW")
    );
    yield* albumReviews.map(makeReview);
  } while (pageToken);
}

function makeReview(video: youtube_v3.Schema$PlaylistItem) {
  const { id, snippet } = video;
  const { title, description, thumbnails, publishedAt } = snippet!;
  const thumbnailUrl = thumbnails?.high?.url;
  const publishDate = publishedAt;
  console.log(title);
  const artist = title!.split(" - ")[0].trim();
  const albumTitle = title!.split(" - ")[1].trim();
  const album = albumTitle.endsWith(" ALBUM REVIEW")
    ? albumTitle.slice(0, -" ALBUM REVIEW".length)
    : albumTitle;
  const ratingMatch = description?.match(/\n(\d+)\/10/);
  const classicMatch = description?.match(/classic\/10/i);
  const rating = ratingMatch ? ratingMatch[1] : classicMatch ? "classic" : null;
  return {
    videoId: id!,
    title: title!,
    artist: artist!,
    album,
    description: description!,
    thumbnailUrl: thumbnailUrl!,
    publishDate: publishDate!,
    watchUrl: `https://www.youtube.com/watch?v=${id}`,
    yellowFlannel: 0,
    rating,
  };
}

export class Reviews {
  constructor(private reviews: AsyncGenerator<InsertReview>) {}

  async until(predicate: (value: InsertReview) => boolean) {
    return new Reviews(this._until(predicate));
  }

  async collect() {
    const newReviews: InsertReview[] = [];
    for await (const review of this.reviews) {
      newReviews.push(review);
    }
    return newReviews;
  }

  private async *_until(
    predicate: (value: InsertReview) => boolean
  ): AsyncGenerator<InsertReview> {
    for await (let value of this.reviews) {
      if (predicate(value)) {
        break;
      }
      yield value;
    }
  }
}
