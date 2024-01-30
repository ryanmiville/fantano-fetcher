"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export function MainNav() {
  const pathname = usePathname();

  return (
    <div className="sticky top-0 z-50 w-full bg-black text-white text-lg">
      <div className="container flex h-20 max-w-screen-2xl items-center">
        <div className="mr-4 hidden md:flex">
          <Link href="/" className="mr-6 flex items-center space-x-2">
            <span className="hidden font-bold text-2xl sm:inline-block ">
              Fantano Fetcher
            </span>
          </Link>
          {/* <nav className="flex items-center gap-6">
            <Link
              href="/docs"
              className={cn(
                "transition-colors hover:text-white/80",
                pathname === "/docs" ? "text-white" : "text-white/60"
              )}
            >
              Docs
            </Link>
            <Link
              href="/docs/components"
              className={cn(
                "transition-colors hover:text-white/80",
                pathname?.startsWith("/docs/components")
                  ? "text-white"
                  : "text-white/60"
              )}
            >
              Components
            </Link>
            <Link
              href="/themes"
              className={cn(
                "transition-colors hover:text-white/80",
                pathname?.startsWith("/themes") ? "text-white" : "text-white/60"
              )}
            >
              Themes
            </Link>
            <Link
              href="/examples"
              className={cn(
                "transition-colors hover:text-white/80",
                pathname?.startsWith("/examples")
                  ? "text-white"
                  : "text-white/60"
              )}
            >
              Examples
            </Link>
            <Link
              href="github.com/ryanmiville/fantano-fetcher"
              className={cn(
                "hidden text-white/60 transition-colors hover:text-white/80 lg:block"
              )}
            >
              GitHub
            </Link>
          </nav> */}
        </div>
      </div>
    </div>
  );
}
