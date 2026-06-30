export type ResearchItem = {
  title: string;
  description: string;
  type: "Working Paper" | "Analysis" | "Dataset" | "Policy Brief";
  authors: string;
  date: string;
};

export const RESEARCH: ResearchItem[] = [
  {
    title: "Toward an African Language Model Benchmark",
    description: "A proposed evaluation suite for measuring frontier model performance across major African languages.",
    type: "Working Paper",
    authors: "Kheir Lissi",
    date: "2026-03",
  },
  {
    title: "Mapping the AU Continental AI Strategy to Technical Workstreams",
    description: "An analysis translating the AU policy framework into concrete research and engineering priorities.",
    type: "Analysis",
    authors: "Kora Lab",
    date: "2026-02",
  },
  {
    title: "Open African Languages Corpus, v0.1",
    description: "An initial release of curated text data across fifteen African languages, openly licensed.",
    type: "Dataset",
    authors: "Kora Lab",
    date: "2026-01",
  },
  {
    title: "Sovereign Compute for African AI: A Policy Brief",
    description: "Recommendations for African governments and the AfDB on building sovereign compute capacity.",
    type: "Policy Brief",
    authors: "Kheir Lissi",
    date: "2025-12",
  },
];
