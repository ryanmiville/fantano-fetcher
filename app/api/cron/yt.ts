import { InsertReview } from "@/db/schema";
import { ChannelVideos, Client, LiveVideo, Video } from "youtubei";
const yt = new Client();
const channelId = "UCt7fwAhXDy3oNFTAzF2o8Pw";

const fmtDate = (date: string) => new Date(date).toISOString().split("T")[0];

export async function getReviews() {
  const channel = await yt.getChannel(channelId);
  const reviews = reviewsGen(channel!.videos);
  return new Reviews(reviews);
}

export async function getReviewsAfter(date: string) {
  const reviews = (await getReviews()).until(
    (review) => fmtDate(review.publishDate) <= date
  );
  const newReviews: InsertReview[] = [];
  for await (const review of reviews) {
    newReviews.push(review);
  }
  return newReviews;
}

async function* reviewsGen(channelVideos: ChannelVideos) {
  const videos = channelVideosGen(channelVideos);
  for await (const v of videos) {
    if (!v.title.endsWith("ALBUM REVIEW")) {
      continue;
    }
    const video = await v.getVideo();
    const review = await makeReview(video);
    yield review;
  }
}

async function* channelVideosGen(channelVideos: ChannelVideos) {
  while (true) {
    const videos = await channelVideos.next(5);
    yield* videos;
  }
}

async function makeReview(video: Video | LiveVideo) {
  const { id, title, description, thumbnails, uploadDate } = video;
  const thumbnailUrl = thumbnails.best!;
  const publishDate = fmtDate(uploadDate);
  const artist = title.split(" - ")[0].trim();
  const albumTitle = title.split(" - ")[1].trim();
  const album = albumTitle.endsWith(" ALBUM REVIEW")
    ? albumTitle.slice(0, -" ALBUM REVIEW".length)
    : albumTitle;
  const ratingMatch = description.match(/\n(\d+)\/10/);
  const classicMatch = description.match(/classic\/10/i);
  const rating = ratingMatch ? ratingMatch[1] : classicMatch ? "classic" : null;
  return {
    videoId: id,
    title,
    artist,
    album,
    description,
    thumbnailUrl,
    publishDate,
    watchUrl: `https://www.youtube.com/watch?v=${id}`,
    yellowFlannel: 0,
    rating,
  };
}

export class Reviews {
  constructor(private reviews: AsyncGenerator<InsertReview>) {}

  async *until(
    predicate: (value: InsertReview) => boolean
  ): AsyncGenerator<InsertReview> {
    for await (let value of this.reviews) {
      if (predicate(value)) {
        break;
      }
      yield value;
    }
  }

  async take(n: number) {
    const reviews: InsertReview[] = [];
    for await (let review of this.reviews) {
      if (n-- === 0) {
        break;
      }
      reviews.push(review);
    }
    return reviews;
  }
}
