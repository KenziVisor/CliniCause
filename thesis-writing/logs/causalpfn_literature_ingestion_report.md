# CausalPFN literature ingestion report

Date: 2026-07-19. Baseline HEAD: `e7edfc3a7d74240c73afa7cf3d1fcfd1678ca4cb`.

The user-supplied `causalPFN.pdf` was verified as a readable, valid PDF (PDF 1.7; 40 pages; `qpdf --check` passed) with SHA-256 `cd3dcd6017745e31db617503f77fa31f6bac454b3be5b3748c4e51d8f5ab3950`. First and last pages were rendered and inspected. The local file is arXiv:2506.07918v2, dated 27 October 2025.

Official NeurIPS proceedings metadata was verified at `papers.nips.cc/paper_files/paper/2025/hash/e3d3db07c1bfb63e1d0b998996de1d12-Abstract-Conference.html`: *CausalPFN: Amortized Causal Effect Estimation via In-Context Learning*, Advances in Neural Information Processing Systems 38, NeurIPS 2025 Main Conference Track. The final author order is Vahid Balazadeh Meresht, Hamidreza Kamkari, Valentin Thomas, Junwei Ma, Bingru Li, Jesse C. Cresswell, Rahul G. Krishnan. The local arXiv PDF uses Vahid Balazadeh, places Benson Li before Junwei Ma, and the final record uses Bingru Li; those differences are recorded rather than merged silently.

The PDF was normalized to `literature/papers/causal_causalpfn_balazadeh_et_al_2025.pdf` without content modification. The attempted `git mv` could not acquire `.git/index.lock` because the sandbox mounts `.git` read-only; the equivalent filesystem rename was used. One BibTeX entry, one core catalog row, and one checksum entry were added. `balazadeh2025causalpfn` is unique; the local PDF hash is unique; catalog/BibTeX/file paths agree; and checksum validation succeeds when run from `thesis-writing/literature/`.

The corpus README now reports 39 core entries, 5 optional entries, 42 valid local PDFs, and 2 missing PDFs. `CIT-GAP-001` is resolved by the citation key; runtime, historical-producing-lineage, local diagnostic, identification, and release gates remain open. The future thesis plan is `planning/causalpfn_thesis_integration_plan.md`.

The AAAI manuscript now cites the final publication in Related Work and at the first method-level CausalPFN mention in Evaluation. External-paper support is limited to method description. Local CliniCause three-estimator agreement remains supported by checked local results. No public-release claim, patient data access, model run, commit, or push occurred.
