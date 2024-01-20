import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { db, reviews } from "@/db";

async function selectReviews() {
  return (await db
    .select({
      artist: reviews.artist,
      album: reviews.album,
      rating: reviews.rating,
      publishDate: reviews.publishDate,
    })
    .from(reviews)
    .limit(10)) as Review[];
}

export type Review = {
  artist: string;
  album: string;
  rating: number | null;
  publishDate: string;
};

export default async function ReviewsTable() {
  const rows = await selectReviews();
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Artist</TableHead>
          <TableHead>Album</TableHead>
          <TableHead>Publish Date</TableHead>
          <TableHead>Rating</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {rows.map((review) => (
          <TableRow key={review.album}>
            <TableCell>{review.artist}</TableCell>
            <TableCell>{review.album}</TableCell>
            <TableCell>{review.publishDate}</TableCell>
            <TableCell>{review.rating}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
