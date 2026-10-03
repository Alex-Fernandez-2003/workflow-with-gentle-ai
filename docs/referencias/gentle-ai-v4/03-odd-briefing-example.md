# ODD Execution Brief — Extended Vertical HU Example

## Purpose

This example demonstrates the desired output for a substantial vertical user story.

It intentionally does **not** pre-create the repository's final technical task list.

The brief transfers product intent, scope, constraints, acceptance, evidence expectations, delivery authorization, and human review boundaries to Pi.

---

## Example input summary

Feature:

`HU-053 — Importar estudiantes mediante CSV`

Known intent:

- A coordinator imports students from CSV.
- Validation must be deterministic and user-visible.
- Invalid rows must not be silently accepted.
- The operation must avoid partial inconsistent imports.
- Existing student/business rules remain authoritative.
- Backend + frontend + tests + evidence may all be involved.
- The user wants local implementation and checks, then Maintainer Review.
- Local commits are allowed.
- Push, PR, merge, and deployment are not allowed yet.
- Exact files/endpoints/schema must be derived by Pi from the repository.

---

# ODD Execution Brief

## 1. Objective

Implement HU-053 so an authorized coordinator can import student records from a CSV file through the existing application, with deterministic validation, clear result reporting, safe persistence behavior, and evidence sufficient for Maintainer Review.

The HU remains one vertical functional outcome even if implementation spans backend, frontend, persistence, tests, documentation, and E2E.

---

## 2. Problem / Why

Manual student creation is inefficient when a coordinator must register many students.

The system needs a bulk path that preserves the same domain rules expected for individual student data while making invalid records visible instead of silently producing inconsistent state.

---

## 3. Authorized Scope

Implementation is authorized for the minimum repository areas necessary to deliver the CSV import outcome, including when repository exploration confirms they are required:

- backend validation/application logic;
- API contract/endpoint integration;
- persistence interaction;
- authorization for the coordinator role;
- frontend upload/result experience;
- relevant automated tests;
- relevant E2E/manual verification;
- permanent HU/requirements/evidence documentation.

Pi may refactor narrowly when needed to reuse an existing validation rule safely.

Any unrelated student-management redesign is outside this authorization.

---

## 4. Non-Goals

- No redesign of the complete student administration module.
- No new generic import framework unless the repository already has one that should be reused.
- No unrelated authentication/role redesign.
- No automatic repair of malformed business data beyond explicitly approved normalization.
- No broad schema rewrite without a demonstrated requirement.
- No push, PR, merge, or deployment before Maintainer Review and explicit authorization.

---

## 5. Sources of Truth

### Product / Scope Authority

1. The current user-approved HU-053 decisions in this briefing.
2. Later explicit Maintainer Review decisions.

### Functional Authority

- Current HU-053 documentation, if present.
- Current student requirements/business rules.
- Existing approved validation decisions.

### Implementation Reality

- Must be established by Pi through repository exploration before implementation details are fixed.

### Technical / Architecture Authority

- Current architecture and repository conventions.
- Existing ADR/technical documentation that remains current.

### Visual Authority

- Approved screenshots/mockups only for the UI elements they actually specify.

### Conflict Rule

If a visual reference conflicts with an explicit functional decision, the explicit functional decision wins.

If documentation and current code disagree about behavior, Pi must report the discrepancy rather than silently deciding that one represents both intended and actual behavior.

---

## 6. Known Project Context

Confirmed from the handoff:

- The operation is a student CSV import.
- The actor is an authorized coordinator.
- The outcome may cross frontend/backend boundaries.
- The HU should remain one vertical functional unit.
- Exact implementation files are intentionally left to repository exploration.
- Permanent documentation/evidence remains part of delivery when the implementation changes project truth.

---

## 7. Current Behavior

The exact current import capability and its repository implementation are not established by this brief.

Pi must determine during exploration:

- whether any CSV import already exists;
- whether student creation/validation is centralized;
- whether an existing DTO/validator/service can be reused;
- current persistence behavior;
- current authorization path;
- current frontend upload patterns;
- current automated/E2E infrastructure.

Do not assume absence or existence before inspection.

---

## 8. Expected Behavior

At minimum, the resulting user flow must support:

1. an authorized coordinator selects a CSV file;
2. the system validates the file/rows against the approved import contract and existing student rules;
3. invalid rows are reported clearly enough to identify what must be corrected;
4. valid processing does not leave silent partial inconsistent state;
5. duplicate/conflicting records follow the approved domain rule;
6. the user receives a deterministic success/failure summary;
7. authorization prevents non-authorized roles from performing the import;
8. the final repository/documentation state reflects the accepted behavior.

Exact UI components, endpoint names, classes, and storage implementation remain repository-derived.

---

## 9. Business Rules

Preserve every current approved student validation rule.

Do not weaken individual-student invariants merely because data arrives in bulk.

Rules that are not explicitly known in this brief must be read from current requirements/repository validation instead of invented.

Bulk processing MUST NOT silently bypass required uniqueness or identity constraints.

If a row cannot be safely normalized under an approved rule, it must be rejected/reported rather than guessed.

---

## 10. Acceptance Criteria

- An authorized coordinator MUST be able to submit a CSV that matches the confirmed import contract.
- The system MUST validate every relevant row before claiming successful import.
- Invalid data MUST produce an observable row/file-level failure report sufficient to locate the problem.
- The import MUST preserve existing student domain invariants.
- Unauthorized actors MUST NOT be able to execute the import.
- The operation MUST NOT leave a state that the user is told is successful when required rows failed silently.
- Duplicate/conflicting students MUST follow the repository's confirmed business rule.
- A successful import MUST be observable in the normal student data flow.
- Applicable automated and/or manual verification MUST be executed and reported from observed results.
- Permanent HU/requirements/evidence documentation MUST be updated if the delivered behavior changes or completes their truth.
- Push, PR creation, merge, and deployment MUST NOT occur before explicit post-review authorization.

Optional scenario notation may be used during execution if it helps test design; it is not required by the briefing format.

---

## 11. Constraints and Invariants

- Preserve existing architecture and validation ownership unless repository evidence justifies a narrow change.
- Avoid introducing a second independent student-validation path.
- Avoid destructive data migration unless it is proven necessary and separately assessed.
- Keep scope limited to HU-053 and dependencies required to deliver it safely.
- Do not convert future enhancements into current scope.
- Treat imported data with the same security/privacy care as manually entered student data.

---

## 12. UX / Visual Expectations

If the repository already contains a project upload/import pattern, prefer consistency with it.

The user must be able to distinguish:

- file selection/readiness;
- validation in progress, when applicable;
- successful completion;
- file-level errors;
- row-level errors where available/appropriate;
- authorization/permission failure.

Do not redesign unrelated desktop/mobile screens.

If visual references are supplied, reproduce their intended behavior/layout without inferring extra features from decorative content.

---

## 13. Known Architecture and Boundaries

No exact files/classes are mandated by this brief.

Known execution constraint:

- preserve the project's current layering and established conventions;
- reuse existing student-validation/domain boundaries where possible;
- keep UI concerns separate from domain validation;
- keep persistence consistency under the repository's existing transaction/data-access model.

Execution responsibility:

Pi must inspect the repository and derive the smallest compatible implementation approach.

---

## 14. Known Contracts and Data

The exact CSV columns, field names, DTOs, endpoint shapes, table names, and error payloads are not invented here.

Pi must reconcile:

- current HU/requirements;
- existing student model;
- current validation;
- any existing import/export format conventions;
- API/frontend conventions.

If the user supplied an approved CSV schema elsewhere, that schema becomes functional authority and must be transferred exactly.

---

## 15. State / Transition Rules

Relevant conceptual states may include:

- file selected;
- validation pending;
- validation failed;
- import ready;
- import executing;
- import completed;
- import failed.

These are conceptual UX/operation states, not required code enums.

Pi should map them onto the existing application model instead of inventing a parallel state machine.

---

## 16. Concurrency / Atomicity / Idempotency Considerations

Repository exploration must determine the actual persistence mechanism.

Required product invariant:

- the operation must not silently report success while leaving an unexpected partial inconsistent batch.

Pi must determine whether the correct behavior is:

- fully atomic batch;
- validated partial import with explicit per-row outcomes;
- another already-approved domain model.

Do not invent transaction/locking technology in the brief.

Repeated submission and duplicate detection must follow confirmed domain rules.

---

## 17. Compatibility / Migration Considerations

Do not assume a migration is needed.

If repository exploration shows persistent schema changes are required:

- preserve existing records;
- define defaults/nullability deliberately;
- preserve backward compatibility where required;
- avoid destructive rollout without explicit approval;
- define rollback/forward-recovery expectations;
- include migration verification.

If no schema change is required, keep migration scope out.

---

## 18. Existing Decisions

- HU-053 remains one vertical functional unit.
- The external briefing does not predefine the final technical task list.
- Pi must derive actual implementation from repository evidence.
- Permanent documentation remains valuable and must be updated when relevant.
- Maintainer Review occurs before remote delivery.
- Local commits are allowed for this example.
- Push, PR, merge, and deployment are not yet allowed.

---

## 19. Material Uncertainties

### RESEARCH REQUIRED

Pi must determine:

- current student validation ownership;
- whether any import capability already exists;
- actual CSV/file handling patterns;
- actual persistence/transaction behavior;
- existing test runners and relevant suites;
- E2E/browser environment availability;
- current HU/evidence documentation paths.

### HUMAN DECISION REQUIRED

Only if repository evidence reveals a product-level ambiguity not already defined, such as two incompatible valid interpretations of duplicate handling or partial-batch semantics.

Do not ask the user to choose files/classes/commands that Pi can determine.

### NON-BLOCKING

Exact implementation paths are intentionally unresolved until exploration.

---

## 20. Test / Verification Context

Known from this brief:

- behavior is suitable for automated testing in at least some layers if the repository has runnable deterministic tests;
- exact runners/commands must be confirmed from the repository;
- E2E availability must be confirmed from the actual environment.

Do not infer commands from framework names.

---

## 21. Verification Expectations

For behavior with meaningful runnable deterministic tests, favor test-first evidence:

RED
→ GREEN
→ REFACTOR

Applicable verification should cover, according to the repository's real infrastructure:

- valid CSV;
- malformed CSV;
- invalid row;
- duplicate/conflict rule;
- authorization;
- persistence consistency;
- result reporting;
- frontend interaction;
- build/typecheck/lint as applicable;
- E2E/manual upload flow when available.

If a runner or environment is unavailable, report it honestly instead of fabricating PASS.

The final evidence summary must distinguish feature failures from known environmental/base failures.

---

## 22. Documentation / Evidence Expectations

Update only documentation affected by the final implementation.

Possible relevant permanent artifacts:

- HU documentation if that is the project's confirmed convention;
- requirements/business-rule documentation;
- API/architecture docs if contracts/architecture truly change;
- evidence manifest;
- screenshots for user-visible import states;
- E2E/manual verification evidence when required by project delivery.

Exact paths must be confirmed from the repository.

Operational ODD tracking must not replace HU/requirements documentation.

---

## 23. Git / Delivery Authorization

| Operation | Authorization | Notes |
| --- | --- | --- |
| Branch create/switch | ALLOWED | Use the project's normal feature-branch convention after inspecting repository state. |
| Worktree creation | ASK | Do not create an additional worktree unless coordination requires it and the user approves. |
| Local commits | ALLOWED | Work-unit commits may be used locally. |
| Push | NOT ALLOWED | Stop before remote publication. |
| PR creation | NOT ALLOWED | Await Maintainer Review. |
| Merge | NOT ALLOWED | Explicit authorization required later. |
| Rebase | ASK | Only if genuinely necessary. |
| Force push | NOT ALLOWED | Never infer permission. |
| Destructive Git operations | NOT ALLOWED | No destructive cleanup/reset without explicit authorization. |
| Deployment | NOT ALLOWED | Separate explicit authorization required. |

Commit permission does not imply push permission.

---

## 24. Stop Conditions / Maintainer Review

Stop when:

- implementation within authorized scope is complete;
- applicable checks have been run;
- unavailable checks are documented;
- permanent documentation/evidence updates are complete;
- local commits are complete only if authorized;
- repository state is ready to present.

Then report:

`IMPLEMENTATION + APPLICABLE CHECKS COMPLETE — PENDING MAINTAINER REVIEW`

Do not:

- push;
- create PR;
- merge;
- deploy;

until explicitly authorized.

---

## 25. Execution Handoff

Pi / Gentle Shell must:

1. use the current ODD workflow;
2. inspect the repository before selecting files, commands, or task breakdown;
3. reconcile this brief with current HU/requirements, repository behavior, and architecture;
4. preserve HU-053 as one vertical product outcome while deriving repository-grounded work units;
5. report out-of-scope findings instead of implementing them;
6. create `odd/tasks/<feature-name>.md` only if the work is substantial after exploration;
7. maintain the project-scoped Engram mirror when available and reconcile both on resume;
8. use test-first RED → GREEN → REFACTOR when a meaningful runnable deterministic behavior test applies;
9. use proportionate observed checks otherwise;
10. update permanent documentation/evidence relevant to the delivered truth;
11. respect Git/delivery authorization exactly;
12. respect existing runtime/user review configuration without changing it;
13. stop at Maintainer Review before remote delivery.

Execution is authorized only within the scope and delivery permissions defined above. Proceed using the current ODD workflow and stop at the configured human decision boundaries.
