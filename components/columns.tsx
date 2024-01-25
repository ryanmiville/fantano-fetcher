"use client";

import { ColumnDef } from "@tanstack/react-table";

import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";
import { Review } from "@/db/schema";
import { MoreHorizontal } from "lucide-react";
import { DataTableColumnHeader } from "./data-table-column-header";

export const ratings = [
  {
    value: "classic",
    label: "Classic",
  },
  {
    value: "10",
  },
  {
    value: "9",
  },
  {
    value: "8",
  },
  {
    value: "7",
  },
  {
    value: "6",
  },
  {
    value: "5",
  },
  {
    value: "4",
  },
  {
    value: "3",
  },
  {
    value: "2",
  },
  {
    value: "1",
  },
  {
    value: "0",
  },
];

export type ReviewColumn = {
  artist: string;
  album: string;
  rating: number | null;
  publishDate: string;
  videoId: string;
};

export const columns: ColumnDef<ReviewColumn>[] = [
  {
    accessorKey: "artist",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Artist" />
    ),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: "album",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Album" />
    ),
    cell: ({ row }) => {
      return (
        <div className="flex space-x-2">
          <span className="max-w-[500px] truncate font-medium">
            {row.getValue("album")}
          </span>
        </div>
      );
    },
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: "rating",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Rating" />
    ),
    cell: ({ row }) => {
      const rating = row.getValue("rating") ?? "---";
      return (
        <div className="flex w-[100px] items-center capitalize">
          <span>{rating}</span>
        </div>
      );
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
  },
  {
    accessorKey: "publishDate",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Publish Date" />
    ),
    cell: ({ row }) => {
      return (
        <div className="flex space-x-2">{row.getValue("publishDate")}</div>
      );
    },
  },
  {
    id: "actions",
    enableHiding: false,
    cell: ({ row }) => {
      const review = row.original;

      return (
        <Dialog>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" className="h-8 w-8 p-0">
                <span className="sr-only">Open menu</span>
                <MoreHorizontal className="h-4 w-4" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DialogTrigger asChild>
                <DropdownMenuItem>Watch Review</DropdownMenuItem>
              </DialogTrigger>
            </DropdownMenuContent>
          </DropdownMenu>
          <DialogContent className="absolute p-9 w-[800px] h-[480px]">
            <iframe
              className="aspect-video w-full h-full"
              src={`https://www.youtube.com/embed/${review.videoId}`}
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </DialogContent>
        </Dialog>
      );
    },
  },
];
