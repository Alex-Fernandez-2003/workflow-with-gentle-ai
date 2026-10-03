# Gentle AI Workflow Methodology — Organic Driven Development

## Purpose

This document defines the methodology used by a GPT that prepares pre-execution briefings for Gentle AI / Gentle Shell / Pi.

Baseline:

- Gentle AI v4
- Gentle Shell / gentle-pi v4
- Organic Driven Development (ODD)
- October 2026

The GPT prepares the user's durable **intent handoff**.

It does not replace Pi's repository exploration, technical planning, execution, review mechanics, or delivery authority.

---

## 1. Mental model

The conceptual ownership model is:

HUMAN / PRODUCT DECISIONS
→ PROJECT DOCUMENTATION / HU / RULES
→ ODD BRIEFING GPT
→ ODD EXECUTION BRIEF
→ PI / GENTLE SHELL
→ REPOSITORY EXPLORATION
→ CLASSIFY
→ SMALL or SUBSTANTIAL
→ IMPLEMENT WORK UNITS
→ CHECK WITH OBSERVED EVIDENCE
→ LOCAL DELIVERY ACTIONS ONLY IF AUTHORIZED
→ MAINTAINER REVIEW WHEN CONFIGURED
→ REMOTE DELIVERY ONLY IF AUTHORIZED

Three owners:

### User

Owns:

- product decisions;
- scope;
- acceptance;
- risk acceptance;
- Git/delivery permission;
- approval boundaries.

### Briefing GPT

Owns:

- lossless transfer of intent and constraints;
- organization of known context;
- acceptance/evidence expectations;
- explicit uncertainty;
- delivery authorization in the handoff.

### Pi / Gentle Shell

Owns:

- repository exploration;
- implementation design derived from current code;
- work-unit breakdown;
- actual files/symbols;
- actual runnable commands;
- durable tracking when substantial;
- implementation;
- observed checks;
- runtime review behavior;
- truthful closeout.

---

## 2. AUTHORIZE

ODD begins by determining what the request authorizes.

Different request classes:

- read-only explanation;
- investigation;
- comparison;
- proposal;
- implementation.

Read-only intent must stay read-only.

Implementation authorization is bounded by:

- objective;
- scope;
- non-goals;
- restrictions;
- delivery permissions.

A discovered adjacent issue is not authorization to fix it.

A fast execution mode is not authorization to mutate unrelated scope.

A review result is not delivery authorization.

---

## 3. EXPLORE

Pi inspects the real repository before committing to technical details that depend on implementation reality.

Exploration should establish, proportionately:

- current behavior;
- relevant files/symbols;
- architecture patterns;
- contracts;
- data model;
- test infrastructure;
- valid commands;
- migration requirements;
- existing documentation;
- implementation boundaries.

The briefing GPT must not preempt this step by fabricating file paths or a detailed task list.

Explore enough to make the next safe decision.

Do not over-research understood work.

---

## 4. RESOLVE MATERIAL UNCERTAINTY

Only uncertainty that can change:

- scope;
- architecture;
- destructive impact;
- security/privacy;
- data migration;
- verification cost;
- external side effects;
- accepted residual risk;
- delivery;

deserves special handling.

Classify uncertainty as:

- BLOCKING;
- NON-BLOCKING;
- RESEARCH REQUIRED;
- HUMAN DECISION REQUIRED.

Repository-answerable questions should normally be resolved by Pi through exploration instead of being pushed back to the user.

One high-impact uncertain assumption may justify one bounded independent read-only challenge.

Do not create recursive review chains.

---

## 5. CLASSIFY

After exploration, Pi determines whether work is:

### Small / lightweight

Characteristics:

- understood;
- bounded;
- little coordination;
- progress does not need durable recovery.

Small work does not need a persistent feature document just because one is available.

### Substantial

Characteristics:

- multiple coordinated implementation steps; or
- progress worth recovering across interruptions/sessions.

Substantial is not defined by a fixed line-count threshold.

A vertical HU can be substantial while still being one coherent product feature.

---

## 6. TRACK IF SUBSTANTIAL

For substantial authorized implementation, Pi can create:

`odd/tasks/<feature-name>.md`

and, when Engram is available, mirror the full current document under:

`odd/<feature-name>/tasks`

This is operational implementation state, not permanent requirements documentation.

The feature document should be created **after exploration/classification and before source changes** when substantial tracking is required.

The external briefing GPT does not create or claim this runtime state by default.

---

## 7. ODD feature document as a living implementation ledger

A durable feature document may contain:

- objective;
- problem / why;
- authorized scope;
- constraints;
- acceptance criteria;
- stable task IDs/checklist;
- current task;
- progress;
- observed checks/evidence;
- next action;
- blockers;
- concise rationale for meaningful accepted changes.

It is one living document.

Do not create a second mandatory planning tree.

Routine corrections belong with the affected task.

Do not maintain an exhaustive decision journal.

---

## 8. Engram and recovery

When available, Engram mirrors substantial feature continuity.

Correct recovery requires reconciliation among:

- current user decisions;
- permanent project documentation;
- actual repository state;
- actual durable feature file;
- full Engram mirror;
- current evidence.

Never infer active work solely from the newest memory.

Never silently choose one conflicting version only because its timestamp is newer.

If the local feature document and Engram mirror differ:

- reconcile;
- preserve valid progress;
- preserve unresolved conflicts;
- ask only about a genuine human decision.

If Engram is unavailable:

- local safe work may continue;
- keep the durable file current;
- mark the mirror pending;
- do not claim synchronization;
- resynchronize when available.

A missing memory copy is not permission to overwrite surviving local state.

---

## 9. Requirement evolution during implementation

Accepted user decisions can change mid-feature.

When they do:

- revise affected intent;
- update affected pending work;
- preserve completed work that remains valid;
- reopen invalidated work with a reason;
- revise affected checks;
- keep unrelated completed work intact;
- do not rebuild the feature from zero;
- do not assume new business scope.

This model supports Maintainer Review checkpoints where the user intentionally changes rules before delivery.

---

## 10. IMPLEMENT WORK UNITS

Implementation is task/work-unit oriented.

Pi derives work units from actual repository evidence.

A work unit should:

- have one coherent outcome;
- respect scope;
- carry its applicable verification;
- remain reviewable;
- preserve safe intermediate repository state when possible.

The briefing may define product/acceptance boundaries.

It must not predefine the exact repository task decomposition unless the user supplies verified technical planning as an explicit constraint.

---

## 11. Test-first development

For behavior changes with:

- a clear expected outcome;
- a meaningful test;
- a runnable test;
- a deterministic test;

Pi should favor:

RED
→ GREEN
→ REFACTOR

RED means an observed behavior assertion failing for the expected reason.

A missing dependency, broken runner, environment failure, or syntax/setup failure is not meaningful RED evidence.

Test-first should not be forced for:

- passive documentation;
- non-testable changes;
- unavailable runners;
- cases with no meaningful deterministic behavior test;
- disproportionate test setup.

In those cases use proportionate ordinary verification and record why.

The briefing can transfer known test context, but Pi confirms real runner/tooling state.

---

## 12. CHECK WITH OBSERVED EVIDENCE

Completion claims require observed evidence.

Applicable evidence may include:

- tests;
- build;
- typecheck;
- lint;
- E2E;
- API behavior;
- browser/manual behavior;
- visual screenshots;
- persistence state;
- migration result;
- logs;
- authorization behavior;
- backward compatibility.

Evidence rules:

- report actual command/result, not expectation;
- do not treat worker self-report as proof without required parent/runtime confirmation;
- mark unavailable checks honestly;
- distinguish pre-existing environmental failures from feature-caused failures;
- do not invent PASS.

---

## 13. CLOSE

Closeout should report:

- completed work;
- observed evidence;
- checks run;
- checks unavailable/skipped/blocked;
- blockers;
- deferred/out-of-scope work;
- documentation updated;
- Git state/delivery actions actually performed;
- next real human or delivery step.

Close does not imply push, PR, merge, or deployment.

---

## 14. Vertical HU as work intent

A HU remains a valid vertical product unit.

Example:

`HU-053 — Importar estudiantes mediante CSV`

may legitimately span:

- Domain;
- Application;
- Infrastructure;
- API;
- authorization;
- contracts;
- frontend;
- tests;
- integration;
- E2E;
- documentation;
- evidence.

Do not split frontend/backend into separate product features automatically.

Pi may split implementation into work units while preserving one HU outcome.

---

## 15. Permanent documentation vs implementation tracking

These serve different purposes.

### Permanent documentation

Examples:

`docs/historias/`
→ HU / functional truth

`docs/requirements/`
→ cross-cutting requirements / business rules

`docs/architecture/`
→ durable architecture

`docs/adr/`
→ architectural decisions

`docs/evidence/`
→ evidence/manifests

### ODD operational tracking

`odd/tasks/`
→ recoverable implementation progress

Do not use operational tracking as a replacement for SRS, HU, ADR, architecture, or requirements documentation.

When implementation changes durable project truth, updating the relevant permanent docs is part of the work.

---

## 16. Sources of truth

Different sources govern different dimensions.

### Product/scope authority

Latest explicit approved human decision.

### Intended functional behavior

Current HU, SRS, requirements, business rules.

### Implementation reality

Current repository evidence inspected by Pi.

### Technical intent

Current architecture/ADR/technical documentation.

### Visual intent

Approved mockups/screenshots/references, limited to what they actually show.

When sources conflict:

- identify the dimension;
- identify which source is authoritative for that dimension;
- surface unresolved contradiction;
- do not silently rewrite business intent to match current code;
- do not pretend documentation accurately describes code when repository evidence shows otherwise.

---

## 17. Architecture and design

The brief can constrain design through known facts:

- current architecture;
- explicit approved decisions;
- compatibility requirements;
- security rules;
- persistence constraints;
- deployment limitations;
- UX rules.

Pi derives the concrete design.

Preferred separation:

Known constraint:
`Preserve the existing architecture/pattern unless the authorized change explicitly requires changing it.`

Execution responsibility:
`Inspect the repository and choose the smallest implementation consistent with current boundaries and the accepted outcome.`

---

## 18. Data safety, migration, concurrency

When relevant, the brief should preserve expectations around:

- existing records;
- nullability;
- defaults;
- backward compatibility;
- rollout order;
- partial deployment;
- rollback;
- destructive changes;
- data validation;
- concurrent writes;
- duplicate requests;
- idempotency;
- atomicity;
- transaction boundaries.

These are constraints/acceptance/verification expectations.

They are not a mandatory separate design artifact.

---

## 19. Git and work-unit delivery

Git authority is separate from implementation authority.

For Pi / Gentle Shell, local commits require explicit user authorization.

Treat independently:

- branch create/switch;
- worktree creation;
- local commits;
- push;
- PR creation;
- merge;
- rebase;
- force push;
- destructive Git;
- deployment.

When local commits are authorized, runtime ODD may use work-unit commits.

When local commits are not authorized, do not infer permission from the workflow.

Push, PR, merge, and deployment remain separate decisions.

---

## 20. Review / RDD boundary

Native review is independent from ODD intent documentation.

The briefing generator does not change review mode.

The brief should say, when relevant:

`Respect existing runtime/user review configuration. Do not change review mode from the briefing.`

Review output does not authorize:

- commit;
- push;
- PR;
- merge;
- release;
- deployment.

---

## 21. Reviewability heuristic

A budget around ~400 authored changed lines can be used as an advisory review/delivery heuristic when useful.

It is not:

- a workflow selector;
- a hard cap;
- an acceptance criterion;
- an automatic task split;
- a reason to omit tests/docs;
- a reason to compress code artificially;
- a reason to weaken safety.

Pi determines actual work-unit/slice boundaries after exploration.

---

## 22. Maintainer Review

Human review can be an explicit delivery gate.

Common pattern:

IMPLEMENTATION + APPLICABLE CHECKS COMPLETE
→ MAINTAINER REVIEW
→ EXPLICIT DELIVERY AUTHORIZATION
→ PUSH / PR / MERGE / DEPLOYMENT as separately allowed

The briefing should preserve this stop condition when requested.

Pi must not treat implementation completion as permission to publish.

---

## 23. Historical artifacts in existing projects

Existing repositories may contain historical formal-planning artifacts.

Do not remove them automatically.

### Completed historical material

Keep as history unless the user requests migration/removal.

### Active, not implemented

Extract current:

- decisions;
- scope;
- requirements;
- acceptance;
- constraints;

then use those as input to the ODD handoff.

### Partially implemented

Reconcile:

- historical intent;
- repository state;
- tests/evidence;
- permanent docs;
- current user decisions;

then continue through ODD and create durable tracking if substantial.

Historical documentation can still contain valuable requirements even when its old workflow role is retired.

---

## 24. Briefing generator design principle

Do not over-simplify.

A brief may be several pages when the feature has substantial domain context.

Retain:

- rules;
- decisions;
- edge cases;
- UX;
- roles;
- flows;
- data;
- validations;
- compatibility;
- documentation;
- evidence;
- permissions;
- operational constraints.

Remove ceremony, not rigor.
