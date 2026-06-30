import { Link, useLocation } from "@tanstack/react-router";
import { useEffect, useState, type ReactNode } from "react";

export const NAV_LINKS = [
  { to: "/", label: "Mission" },
  { to: "/approach", label: "Approach" },
  { to: "/research", label: "Research" },
  { to: "/blog", label: "Blog" },
  { to: "/about", label: "About" },
  { to: "/resources", label: "Resources" },
  { to: "/contact", label: "Contact" },
] as const;

export function useReveal() {
  const location = useLocation();
  useEffect(() => {
    const els = document.querySelectorAll<HTMLElement>(".kora-reveal");
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("is-visible");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12 },
    );
    els.forEach((el) => io.observe(el));
    return () => io.disconnect();
  }, [location.pathname]);
}

function Nav() {
  const [open, setOpen] = useState(false);
  const location = useLocation();
  useEffect(() => { setOpen(false); }, [location.pathname]);

  return (
    <>
      <nav className="sticky top-0 z-50 w-full border-b border-[#E8E8E8] bg-white/95 backdrop-blur">
        <div className="mx-auto flex h-16 max-w-[1100px] items-center justify-between px-6">
          <Link to="/" className="kora-wordmark text-[#0A0A0A]">KORA LAB</Link>
          <div className="hidden items-center gap-7 md:flex">
            {NAV_LINKS.map((l) => (
              <Link
                key={l.to}
                to={l.to}
                activeOptions={{ exact: l.to === "/" }}
                className="text-sm text-[#0A0A0A] transition-opacity hover:opacity-60 [&[data-status=active]]:border-b [&[data-status=active]]:border-[#0A0A0A] [&[data-status=active]]:pb-0.5"
              >
                {l.label}
              </Link>
            ))}
          </div>
          <Link
            to="/contact"
            className="hidden bg-[#0A0A0A] px-5 py-2.5 text-xs font-bold uppercase tracking-wider text-white transition-opacity hover:opacity-80 md:inline-block"
          >
            Get in Touch
          </Link>
          <button
            type="button"
            aria-label="Open menu"
            onClick={() => setOpen((o) => !o)}
            className="flex h-10 w-10 flex-col items-center justify-center gap-1.5 rounded-full bg-white/90 md:hidden"
          >
            <span className="block h-0.5 w-5 bg-[#0A0A0A]" />
            <span className="block h-0.5 w-5 bg-[#0A0A0A]" />
            <span className="block h-0.5 w-5 bg-[#0A0A0A]" />
          </button>
        </div>
      </nav>
      {open && (
        <div className="fixed inset-0 top-16 z-40 flex flex-col gap-6 bg-[#0A0A0A] px-6 py-12 md:hidden">
          {NAV_LINKS.map((l) => (
            <Link
              key={l.to}
              to={l.to}
              className="text-3xl font-black tracking-[-0.02em] text-white"
            >
              {l.label}
            </Link>
          ))}
          <Link
            to="/contact"
            className="mt-4 inline-block self-start bg-white px-6 py-3 text-xs font-bold uppercase tracking-wider text-[#0A0A0A]"
          >
            Get in Touch
          </Link>
        </div>
      )}
    </>
  );
}

function Footer() {
  return (
    <footer className="bg-[#0A0A0A] text-white">
      <div className="mx-auto max-w-[1100px] px-6 py-16">
        <div className="grid gap-10 md:grid-cols-3">
          <div>
            <p className="kora-wordmark">KORA LAB</p>
            <p className="mt-3 text-sm text-[#ABABAB]">Africa's Sovereign AI Lab</p>
            <p className="mt-1 text-sm text-[#6B6B6B]">Lome, Togo</p>
          </div>
          <div className="flex flex-col gap-2 md:items-center">
            {NAV_LINKS.map((l) => (
              <Link key={l.to} to={l.to} className="text-xs font-bold uppercase tracking-wider text-[#ABABAB] hover:text-white">
                {l.label}
              </Link>
            ))}
            <Link to="/glossary" className="text-xs font-bold uppercase tracking-wider text-[#ABABAB] hover:text-white">
              Glossary
            </Link>
          </div>
          <div className="md:text-right">
            <p className="text-sm text-white">Building for the continent.</p>
            <div className="mt-3 flex flex-col gap-1 text-sm text-[#ABABAB] md:items-end">
              <a href="https://koralab.org" className="hover:text-white">koralab.org</a>
              <a href="https://edenvallie.com" className="hover:text-white">edenvallie.com</a>
            </div>
          </div>
        </div>
        <div className="mt-12 border-t border-[#1A1A1A] pt-6 text-xs text-[#6B6B6B]">
          © {new Date().getFullYear()} Kora Lab. All rights reserved.
        </div>
      </div>
    </footer>
  );
}

export function SiteLayout({ children }: { children: ReactNode }) {
  useReveal();
  return (
    <div className="flex min-h-screen flex-col bg-white text-[#0A0A0A]">
      <Nav />
      <main className="flex-1">{children}</main>
      <Footer />
    </div>
  );
}

export function SectionLabel({ children }: { children: ReactNode }) {
  return (
    <p className="text-[9px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">{children}</p>
  );
}
