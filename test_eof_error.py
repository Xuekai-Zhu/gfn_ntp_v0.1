from lean_dojo import *
from proof_flow.src.utils import prepare_environment_for_lean_dojo, repo_root

#command: /home/zhuxuekai/.elan/bin/lake
# args: [b'/home/zhuxuekai/.elan/bin/lake', b'env', b'lean', b'--threads=1', b'--memory=32768', b'Mathlib/Data/Relqk2dq38z.lean']
#

repo = LeanGitRepo(
    "https://github.com/leanprover-community/mathlib4",
    "29dcec074de168ac2bf835a77ef68bbe069194c5",
)
traced_file = traced_repo.get_traced_file("Mathlib/Data/Relqk2dq38z.lean")