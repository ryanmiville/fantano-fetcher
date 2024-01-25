import {
  date,
  int,
  mysqlTable,
  primaryKey,
  text,
  tinyint,
  unique,
  varchar,
} from "drizzle-orm/mysql-core";

export const reviews = mysqlTable(
  "reviews",
  {
    id: int("id").autoincrement().notNull(),
    videoId: varchar("video_id", { length: 255 }).notNull(),
    title: varchar("title", { length: 255 }).notNull(),
    artist: varchar("artist", { length: 255 }).notNull(),
    album: varchar("album", { length: 255 }).notNull(),
    description: text("description").notNull(),
    thumbnailUrl: varchar("thumbnail_url", { length: 255 }).notNull(),
    // you can use { mode: 'date' }, if you want to have Date as type for this column
    publishDate: date("publish_date", { mode: "string" }).notNull(),
    watchUrl: varchar("watch_url", { length: 255 }).notNull(),
    yellowFlannel: tinyint("yellow_flannel"),
    rating: varchar("rating", { length: 255 }),
  },
  (table) => {
    return {
      reviewsId: primaryKey({ columns: [table.id], name: "reviews_id" }),
      videoId: unique("video_id").on(table.videoId),
    };
  }
);

export type Review = typeof reviews.$inferSelect;
