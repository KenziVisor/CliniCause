# Stage 4 Writing Order

Do not draft in chapter-number order by default. Start with stable methods and contracts, then results, then synthesis.

| draft_order | section | why_now | required_evidence | blocking_dependencies | expected_output_file | review_focus |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | C3.1 Units, time horizons, and data objects | Stable definitions anchor every later chapter. | preprocessing contracts; STraTS loader; terminology plan | none | `thesis-writing/thesis/chapters/ch03_problem_definition.tex` | Correct unit/ID/artifact terminology. |
| 2 | C4 Data and preprocessing | Implementation-grounded and low result risk. | preprocessing scripts; configs; dataset citations | processed counts remain placeholders | `chapters/ch04_data_preprocessing.tex` | Contract accuracy and no invented counts. |
| 3 | C5.1-C5.3 Rule-based proxy construction | Central contribution; source-backed. | tagger scripts; proxy table plan; LLM prompt-provenance audit; clinical citations | advisor clinical wording and prompt-review record | `chapters/ch05_proxy_states.tex` | Proxy vs diagnosis language; prompt outputs as design provenance only. |
| 4 | C5.4 Majority vote and predicted proxy-state sources | Bridges prediction and causal pipeline. | majority vote/split/export scripts; audit | voter manifest [PROVENANCE UNCLEAR] | same chapter or `chapters/ch05_proxy_states.tex` | Do not call majority vote consensus truth. |
| 5 | C6 Predictive modeling methods | Model code is stable; results can remain deferred. | STraTS source; model citations; wrappers | InterpNet result status | `chapters/ch06_predictive_modeling.tex` | Multi-label task and metric definitions. |
| 6 | C7 Causal graph and effect-estimation methods | Method assumptions must be settled before results. | DAG/CATE/matching source; causal citations | advisor intervention/estimand gate | `chapters/ch07_causal_methods.tex` | Causal wording under assumptions. |
| 7 | C8 Robustness/sensitivity/validation design | Can be drafted before numerical conclusions. | sensitivity/permutation/matching code; citations | per-treatment result validation for examples | `chapters/ch08_validation_design.tex` | Diagnostic vs proof language. |
| 8 | C9 Experimental design | Design matrix organizes result extraction. | experiment inventory; wrappers; run summaries | primary estimator/sampling decision | `chapters/ch09_experimental_design.tex` | Distinguish implemented/executed/missing. |
| 9 | Appendix A/B proxy/DAG details | Supports advisor review of methods. | tagger and graph source | clinical review | `appendices/proxy_and_dag_details.tex` | Completeness without main-text overload. |
| 10 | Results tables extraction plan and checked tables | Needed before C10 prose. | all selected result artifacts | manifest/config decisions; advisor result scope | `thesis-writing/tables/*.csv` or `.tex` later | Numeric provenance and row selection. |
| 11 | C10 Results | Only after checked tables/figures exist. | validated tables/figures | missing result/provenance blockers | `chapters/ch10_results.tex` | No invented placeholders as results. |
| 12 | C11 Discussion | Depends on stable result claims. | C10; limitations matrix; literature | result approval | `chapters/ch11_discussion.tex` | Balanced interpretation and limitations. |
| 13 | C1 Introduction | Easier after body contribution boundaries are fixed. | completed C3-C11 summary | advisor story/title approval | `chapters/ch01_introduction.tex` | No overpromise. |
| 14 | C2 Background and related work | Can be drafted late to align with final scope. | citation plan; methods chapters | citation gap CausalPFN | `chapters/ch02_background.tex` | Synthesis, not paper list. |
| 15 | C12 Conclusions and future work | Last main chapter. | final results/discussion | all major review gates | `chapters/ch12_conclusions.tex` | No new evidence. |
| 16 | Abstracts, keywords, acknowledgements, front matter | Final thesis summary must match final body. | completed thesis | BGU language/order approval | `frontmatter/*.tex` | <=500-word abstracts, keyword count. |

Human approval gates:

- Gate A after drafts 1-4: data/proxy-state terminology and clinical wording.
- Gate B after drafts 5-8: prediction/causal methods and estimand wording.
- Gate C before draft 10: approved result artifacts, manifest, primary estimator/sampling decision.
- Gate D after C10: result interpretation approval.
- Gate E after C11-C12 and intro/background: full narrative approval.
- Gate F before front matter: title, language, administrative pages.
