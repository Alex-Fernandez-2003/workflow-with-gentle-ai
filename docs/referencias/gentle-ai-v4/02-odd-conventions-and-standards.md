# ODD Briefing Conventions and Standards

## Purpose

This document defines quality standards for pre-execution ODD briefings generated for Pi / Gentle Shell.

The briefing must be:

- technically precise;
- scope-safe;
- evidence-aware;
- detailed without inventing implementation;
- useful across frontend, backend, mobile, data, DevOps, CI/E2E, and academic projects;
- self-sufficient without hidden memory.

---

## 1. Language policy

Match the user's language unless explicitly requested otherwise.

Spanish input → Spanish output.

English input → English output.

Preserve exact:

- filenames;
- commands;
- UI labels;
- errors;
- domain names;
- identifiers;

when they are evidence.

---

## 2. Writing policy

Prefer:

- concrete facts;
- explicit constraints;
- measurable acceptance;
- concise rationale;
- scoped uncertainty.

Avoid:

- marketing language;
- filler;
- generic "best practices" detached from the project;
- speculative file names;
- speculative architecture;
- empty sections;
- duplicated content across many headings;
- artificial process language.

---

## 3. Repository-awareness rule

If repository content was not actually supplied or inspected, do not write:

`Modify XService.cs`

or:

`Update POST /api/foo`

unless those are confirmed by user-provided evidence.

Use:

- likely functional area;
- known layer;
- known flow;
- exact implementation location unresolved.

If a repository/file tree is supplied, use only details supported by it.

---

## 4. Fact taxonomy

Every relevant statement should fit one of:

### Confirmed fact

Supported by supplied evidence.

### User decision

Explicitly approved by the user.

### Assumption

Necessary but unconfirmed.

Keep assumptions minimal.

### Expected behavior

Observable desired outcome.

### Material uncertainty

Unknown that could change execution materially.

### Execution responsibility

Something Pi must determine from the repository.

Do not blur these categories.

---

## 5. Authorization standard

The brief must make mutation authority legible.

Separate:

- exploration allowed;
- implementation allowed;
- documentation updates allowed;
- local Git allowed;
- remote Git allowed;
- deployment allowed.

A request to inspect does not authorize edits.

A request to implement does not automatically authorize:

- commit;
- push;
- PR;
- merge;
- deploy.

---

## 6. Sources of Truth standard

Use the section when multiple inputs exist.

Recommended shape:

## Sources of Truth

### Product / Scope Authority
- ...

### Functional Authority
- ...

### Business Rules
- ...

### Implementation Reality
- To be established from repository exploration, or list confirmed repository evidence.

### Technical / Architecture Authority
- ...

### Visual References
- ...

### Conflict Rule
- ...

Visual references do not silently create product requirements.

Historical documents should be labeled historical when not current.

---

## 7. Current vs expected behavior

When useful, separate:

### Current Behavior

Only confirmed current behavior.

### Expected Behavior

Desired observable behavior.

Do not invent current behavior from the desired feature.

---

## 8. Business-rule standard

Rules should preserve exact domain meaning.

Good:

`A student MAY have multiple historical tutoring records, but the current degree-tutoring invariant remains one active student per tutoring record unless the user approves a future cardinality change.`

Bad:

`Keep relationships correct.`

If a numeric validation is known, preserve it exactly.

If unknown, do not invent a reasonable range.

---

## 9. Acceptance criteria

Acceptance criteria must be:

- specific;
- observable;
- verifiable;
- tied to scope;
- implementation-neutral when possible.

Optional precision tools:

- MUST;
- SHOULD;
- MAY;
- Given / When / Then.

Use them when they improve clarity, not by ritual.

Bad:

`The UI should look good.`

Better:

`At the project's confirmed mobile breakpoint, each product MUST use the approved card representation while the desktop presentation remains unchanged.`

---

## 10. Edge cases

Only include edge cases relevant to the feature.

Common categories to consider:

- empty input;
- null/missing data;
- zero values;
- negative values;
- duplicates;
- stale state;
- nonexistent resource;
- inactive resource;
- authorization failure;
- invalid transition;
- repeated request;
- decimal/rounding;
- date/timezone;
- concurrency;
- partial failure;
- dependency failure;
- legacy data;
- large input;
- responsive layout.

Do not dump a generic list into every brief.

---

## 11. UX / visual standard

When frontend/mobile/UI work is involved, capture:

- current presentation if known;
- target presentation;
- reference images/mockups;
- responsive expectations;
- interaction preservation;
- loading/empty/error/disabled/success states;
- accessibility constraints when relevant;
- explicit non-goals.

Mockups are visual authority only for what is actually visible/approved.

They do not automatically authorize backend or business-rule changes.

---

## 12. Known architecture and boundaries

Capture only known architecture.

Useful content:

- architecture style;
- stack;
- layer boundaries;
- cross-layer invariants;
- existing patterns that must be preserved;
- explicit technical decisions.

Do not convert this into an implementation recipe unless the user explicitly supplied one.

---

## 13. Contracts and data

Record confirmed:

- request/response shapes;
- DTO/interface expectations;
- persisted fields;
- schema constraints;
- events;
- file formats;
- external integration behavior;
- compatibility guarantees.

If unknown:

`Exact contract must be confirmed during repository exploration.`

Do not invent API shapes.

---

## 14. State and transitions

For stateful workflows, document:

- relevant states;
- allowed transitions;
- forbidden transitions;
- transition guards;
- authorization rules;
- observable side effects.

Use a compact transition table when it clarifies the feature.

---

## 15. Concurrency / atomicity / idempotency

Consider when the feature can receive overlapping operations.

Examples:

- duplicate submission;
- double confirmation/cancellation;
- simultaneous stock movement;
- two assignments to one resource;
- retries;
- stale updates;
- partial batch failure.

Capture the expected invariant, not a fabricated locking mechanism.

Good:

`The batch MUST be atomic from the user's perspective: either all accepted rows are persisted or none are.`

Avoid:

`Use advisory lock X`

unless explicitly approved/confirmed.

---

## 16. Migration and data safety

For persistent data changes, consider:

- existing records;
- defaults;
- nullability;
- backfill;
- backward compatibility;
- rollout order;
- partial deployment;
- destructive operations;
- rollback;
- validation of legacy/new data;
- indexes/constraints only when known as requirements.

Do not invent a migration file or ORM command.

---

## 17. Test / verification context

Record only known information:

- existing test layers;
- known runner commands;
- E2E environment constraints;
- platform differences;
- known unavailable environments;
- known pre-existing failures.

Do not infer command syntax from stack names.

Do not convert "tests exist" into "test-first definitely applies."

---

## 18. Test-first applicability

For a behavior change, favor RED → GREEN → REFACTOR when all are true:

- expected behavior is clear;
- a meaningful behavior test can be written;
- the test is runnable;
- the result is deterministic enough to be useful.

Do not force RED from:

- missing dependencies;
- broken environment;
- unrelated base failures;
- non-testable documentation;
- visual-only behavior without a meaningful deterministic automated assertion.

When test-first does not apply, require proportionate verification and state why.

---

## 19. Verification expectations

Specify expected evidence without claiming it exists.

Examples:

- relevant unit test result;
- focused integration result;
- build result;
- typecheck/lint result;
- E2E result;
- manual browser flow;
- responsive screenshots;
- DB state;
- logs;
- API response;
- permission-denial case;
- rollback/migration check.

For unavailable checks, require truthful reporting.

---

## 20. Documentation / evidence expectations

Explicitly distinguish permanent docs from implementation tracking.

Possible permanent updates:

- HU;
- SRS;
- requirements;
- architecture;
- ADR;
- API docs;
- deployment docs;
- evidence manifests;
- screenshots;
- diagrams;
- academic deliverables.

Only request updates that the feature actually changes.

---

## 21. Git / Delivery Authorization format

Recommended table:

| Operation | Authorization | Notes |
| --- | --- | --- |
| Branch create/switch | ALLOWED / NOT ALLOWED / ASK | ... |
| Worktree creation | ALLOWED / NOT ALLOWED / ASK | ... |
| Local commits | ALLOWED / NOT ALLOWED / ASK | ... |
| Push | ALLOWED / NOT ALLOWED / ASK | ... |
| PR creation | ALLOWED / NOT ALLOWED / ASK | ... |
| Merge | ALLOWED / NOT ALLOWED / ASK | ... |
| Rebase | ALLOWED / NOT ALLOWED / ASK | ... |
| Force push | ALLOWED / NOT ALLOWED | ... |
| Destructive Git operations | ALLOWED / NOT ALLOWED | ... |
| Deployment | ALLOWED / NOT ALLOWED / ASK | ... |

Never map one permission onto another.

For Pi / Gentle Shell, local commits require explicit permission.

---

## 22. Maintainer Review format

When required:

## Stop Conditions / Maintainer Review

- Stop after: implementation + applicable checks + documentation/evidence updates.
- Do not push.
- Do not create PR.
- Do not merge.
- Do not deploy.
- Present the local state and evidence for Maintainer Review.
- Resume delivery only after explicit authorization.

Adapt to user policy.

---

## 23. Material uncertainty standard

Avoid generic "Open Questions."

Use:

### BLOCKING

Only decisions without which safe execution cannot proceed.

### RESEARCH REQUIRED

Questions Pi should answer from repository/documentation/tooling evidence.

### HUMAN DECISION REQUIRED

Product/scope/risk choices that Pi must not decide.

### NON-BLOCKING

Useful uncertainty that does not prevent starting.

Do not ask the user for something Pi can safely determine from repository exploration.

---

## 24. ODD durable tracking rule

The briefing may explain to Pi:

- classify work after exploration;
- if substantial, create/maintain one durable feature document;
- if small, keep it lightweight.

The external GPT does not pre-generate the repository-derived checklist.

Do not pretend the durable file or memory mirror already exists.

---

## 25. Engram rule

The briefing may state:

`For substantial work, maintain the runtime's project-scoped recovery mirror when Engram is available and reconcile it with the actual feature document on resume.`

Do not claim:

- memory saved;
- memory synchronized;
- memory is current.

Do not make the brief depend on memory.

---

## 26. Requirement-change rule

If the user changes a decision later:

- update affected intent;
- update affected pending work;
- preserve valid completed work;
- reopen invalidated work with reason;
- revise checks;
- do not expand scope silently.

---

## 27. Review / RDD rule

The brief does not control native review mode.

Preferred wording:

`Respect existing runtime/user review configuration. Do not enable or disable review mode from this briefing.`

A review result does not authorize delivery.

---

## 28. Reviewability heuristic

Approximately ~400 authored changed lines may be useful as an advisory review/delivery budget.

Do not use it as:

- a hard task limit;
- a workflow switch;
- an acceptance criterion.

Do not sacrifice tests, docs, readability, or correctness to meet the number.

Pi derives actual boundaries.

---

## 29. Security and privacy

Never request or reproduce secrets unnecessarily.

If a secret/token/key appears:

- avoid repeating it;
- refer to it generically;
- recommend rotation when exposure is plausible;
- preserve least-privilege and authorization boundaries.

For production data:

- avoid copying sensitive records into briefs;
- describe shapes/rules instead.

---

## 30. Handoff quality

A good Execution Handoff is specific to the change.

It should not simply say:

`Implement this feature.`

It should transfer:

- scope;
- product decisions;
- required behavior;
- invariant constraints;
- evidence expectations;
- permanent documentation obligations;
- Git boundaries;
- human stop conditions;

while leaving repository-derived implementation planning to Pi.

---

## 31. Quality checklist

- [ ] No unsupported repository detail was invented.
- [ ] Scope is explicit.
- [ ] Non-goals are explicit.
- [ ] Sources of truth are clear when relevant.
- [ ] Current and expected behavior are not conflated.
- [ ] Business rules are precise.
- [ ] Acceptance is testable/observable.
- [ ] Edge cases are relevant, not boilerplate.
- [ ] Architecture is constrained, not fabricated.
- [ ] Data/migration/concurrency concerns are captured when relevant.
- [ ] Test-first applicability is conditional and evidence-based.
- [ ] Verification expectations do not claim PASS.
- [ ] Permanent documentation expectations are explicit when relevant.
- [ ] Git permissions are independent.
- [ ] Local commits are not assumed.
- [ ] Push/PR/merge/deployment are not assumed.
- [ ] Review mode is not changed.
- [ ] Maintainer Review is preserved when requested.
- [ ] Durable ODD tracking is left to Pi after exploration.
- [ ] The brief remains rigorous without becoming a phase ceremony.
