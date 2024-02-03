import { InsertReview } from "@/db/schema";
import { ChannelVideos, Client, LiveVideo, Video } from "youtubei";
const yt = new Client();
const channelId = "UCt7fwAhXDy3oNFTAzF2o8Pw";

const fmtDate = (date: string) => new Date(date).toISOString().split("T")[0];

export async function getReviewsAfter(date: string) {
  const channel = await yt.getChannel(channelId);
  if (!channel) {
    return null;
  }
  const videos = videoGen(channel.videos);
  let reviews: InsertReview[] = [];
  for await (const v of videos) {
    if (!v.title.endsWith("ALBUM REVIEW")) {
      continue;
    }
    const video = await v.getVideo();
    if (fmtDate(video.uploadDate) <= date) {
      break;
    }
    const review = await makeReview(video);
    reviews.push(review);
  }
  return reviews;
}

async function* videoGen(channelVideos: ChannelVideos) {
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
