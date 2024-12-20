LLEMMA_4S_PROMPT = """Given the Lean 4 tactic state, suggest a next tactic.
Here are some examples:

Tactic state:
---
α : Type u_1
r : α → α → Prop
inst✝¹ : DecidableEq α
inst✝ : IsIrrefl α r
⊢ CutExpand r ≤ InvImage (Finsupp.Lex (rᶜ ⊓ fun x x_1 => x ≠ x_1) fun x x_1 => x < x_1) ↑toFinsupp
---
Next tactic:
---
rintro s t ⟨u, a, hr, he⟩
---

Tactic state:
---
ι : Type u_1
I✝ J✝ : Box ι
x y : ι → ℝ
I J : WithBot (Box ι)
⊢ ↑I = ↑J ↔ I = J
---
Next tactic:
---
simp only [Subset.antisymm_iff, ← le_antisymm_iff, withBotCoe_subset_iff]
---

Tactic state:
---
m n : ℕ
h : Nat.coprime m n
⊢ Nat.gcd m n = 1
---
Next tactic:
---
rw [← h.gcd_eq_one]
---

Tactic state:
---
{state}
---
Next tactic:
---""" 

def _llemma_prompt_fewshot(ts):
    return LLEMMA_4S_PROMPT.format(state=ts)

INSTRUCTION_TEMPLATE = """Given the Lean 4 tactic state, suggest a next tactic.

Tactic state:
---
{state}
---
Next tactic:
---
{target}
"""

INSTRUCTION_PROMPT_TEMPLATE = """Given the Lean 4 tactic state, suggest a next tactic.

Tactic state:
---
{state}
---
Next tactic:
---
"""

INSTRUCTION_COMPLETION_TEMPLATE = "{tactic}"

INSTRUCTION_COMPLETION_TEMPLATE_WITH_NEXT_STATE = """{tactic}
---
Resulting state:
---
{next_state}
"""

# reward model prompt and completion templates
# - reward is computed from the log probability of the completion given the prompt

# llemma model
LLEMMA_RM_ST_PROMPT_TEMPLATE = """Given the Lean 4 tactic state, suggest a next tactic.

Tactic state:
---
{state}
---
Next tactic:
---
"""
LLEMMA_RM_ST_COMPLETION_TEMPLATE = "{tactic}"
LLEMMA_RM_STS_PROMPT_TEMPLATE = """From the Lean 4 tactic state

Tactic state:
---
{state}
--- 
Does the next tactic and its resulting state make progress towards completing the proof?

Next tactic:
---
{tactic}
---
Resulting state (None means the tactic failed):
---
{next_state}
---
Answer: """
LLEMMA_RM_STS_PROMPT_TEMPLATE_V2 = """Consider the following Lean 4 tactic state, tactic, and resulting state.

Tactic state:
---
{state}
---
Candidate tactic:
---
{tactic}
---
Resulting tactic state:
---
{next_state}
---
Did the tactic make progress towards completing the proof?
Answer: """
LLEMMA_RM_STS_COMPLETION_TEMPLATE = "yes"

# deepseek model
# - copied markdown-like code blocks from 
#   `DeepSeek-Prover-V1.5/prover/utils.py`'s prompts
DEEPSEEK_RM_ST_PROMPT_TEMPLATE = """Given the following Lean 4 proof state
```
{state}
```
suggest a next tactic.
```lean4
"""
DEEPSEEK_RM_ST_COMPLETION_TEMPLATE = "{tactic}"
DEEPSEEK_RM_STS_PROMPT_TEMPLATE = """Given a Lean 4 proof state, tactic, and resulting state, did the tactic make progress towards completing the proof?
```lean4
-- proof state
/-
{state}
-/
-- tactic
/-
{tactic}
-/
-- resulting state (None means the tactic failed)
/-
{next_state}
-/
```
Answer: """
DEEPSEEK_RM_STS_COMPLETION_TEMPLATE = "yes"
DEEPSEEK_RM_ST_PROMPT_TEMPLATE_V2 = """Suggest a next tactic given the following Lean 4 tactic state
```lean4
-- tactic state
/-
{state}
-/
-- next tactic
"""
DEEPSEEK_RM_ST_COMPLETION_TEMPLATE_V2 = """{tactic}
```"""
DEEPSEEK_RM_ST_PROMPT_TEMPLATE_V3 = """Given the following Lean 4 tactic state:
```
{state}
```
Suggest a next tactic.
```lean4
"""
PROOF_SEARCH_IDENTITY_TEMPLATE = "{state}"
REPROVER_TACGEN_PROMPT_TEMPLATE = "{state}"
REPROVER_TACGEN_COMPLETION_TEMPLATE = "{tactic}"
REPROVER_RM_STS_PROMPT_TEMPLATE = """-- state
{state}
-- tactic
{tactic}
-- next state
{next_state}
-- question
Does the tactic make progress towards completing the proof (y/n)?"""

REPROVER_TACGEN_WITH_HISTORY = """initial state:
{initial_state}
tactics:
{tactics}
current state:
{current_state}"""

RM_TEMPLATES = {
    "llemma": {
        "st": {
            "prompt": LLEMMA_RM_ST_PROMPT_TEMPLATE,
            "completion": LLEMMA_RM_ST_COMPLETION_TEMPLATE,
        },
        "sts": {
            "prompt": LLEMMA_RM_STS_PROMPT_TEMPLATE,
            "completion": LLEMMA_RM_STS_COMPLETION_TEMPLATE,
        },
    },
    "deepseek": {
        "st": {
            "prompt": DEEPSEEK_RM_ST_PROMPT_TEMPLATE_V2,
            "completion": DEEPSEEK_RM_ST_COMPLETION_TEMPLATE_V2,
        },
        "sts": {
            "prompt": DEEPSEEK_RM_STS_PROMPT_TEMPLATE,
            "completion": DEEPSEEK_RM_STS_COMPLETION_TEMPLATE,
        },
    },
    "reprover": {
        "st": {
            "prompt": REPROVER_TACGEN_PROMPT_TEMPLATE,
            "completion": REPROVER_TACGEN_COMPLETION_TEMPLATE,
        },
        "sts": {
            "prompt": REPROVER_RM_STS_PROMPT_TEMPLATE,
            "completion": "y",
        }
    }
}

PROMPT_DICT = {
    "ds_rm_st_v2": DEEPSEEK_RM_ST_PROMPT_TEMPLATE_V2,
    "identity": PROOF_SEARCH_IDENTITY_TEMPLATE,
    "reprover_tacgen_with_history": REPROVER_TACGEN_WITH_HISTORY,
}
