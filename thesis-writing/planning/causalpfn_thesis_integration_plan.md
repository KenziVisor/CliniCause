# CausalPFN thesis-integration plan

## Verified record

- Citation key: `balazadeh2025causalpfn`
- Canonical local PDF: `thesis-writing/literature/papers/causal_causalpfn_balazadeh_et_al_2025.pdf`
- SHA-256: `cd3dcd6017745e31db617503f77fa31f6bac454b3be5b3748c4e51d8f5ab3950`
- Publication: Vahid Balazadeh Meresht, Hamidreza Kamkari, Valentin Thomas, Junwei Ma, Bingru Li, Jesse C. Cresswell, and Rahul G. Krishnan. *CausalPFN: Amortized Causal Effect Estimation via In-Context Learning.* Advances in Neural Information Processing Systems 38, NeurIPS 2025 Main Conference Track.
- Local-version boundary: the retained PDF is arXiv:2506.07918v2 dated 27 October 2025. It lists Vahid Balazadeh and Benson Li, while the final proceedings use Vahid Balazadeh Meresht and Bingru Li and place Junwei Ma before Bingru Li.

## Approved method claims

The source may support a bounded description of CausalPFN as a prior-data-fitted/in-context model that amortizes causal-effect estimation after training on simulated identifiable data-generating processes. It may support CausalPFN as a method-level comparator with a modeling paradigm distinct from the project DML estimators.

It must not be used to claim that CliniCause proxy states are valid, that the project DAG/observational assumptions hold, that local numerical effects are validated, or that CausalPFN has diagnostic parity with the project DML analyses. The local `18/19` directional-agreement result is supported only by checked CliniCause aggregate outputs.

## Recommended thesis locations

| Location | Proposed bounded use |
| --- | --- |
| C2.4 Related Work | Situate prior-data-fitted/in-context causal-effect estimation alongside DML and forest methods. |
| C7 Causal methodology | Cite the method when introducing the CausalPFN branch and retain local implementation/provenance boundaries. |
| C9 Experimental design | Identify CausalPFN as a complementary estimator in the comparison matrix, not as evidence for local identification. |
| C10 Results | Cross-reference the method citation only where needed to orient the estimator; cite checked project output for numerical findings. |
| C11 Discussion and limitations | Explain its distinct modeling perspective while retaining the smaller archived diagnostic envelope. |

No thesis chapter prose was edited during P8. Future integration should use the above key and preserve the distinction between external method evidence and local CliniCause empirical evidence.
