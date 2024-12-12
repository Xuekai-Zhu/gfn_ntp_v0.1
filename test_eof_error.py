from lean_dojo import *
from proof_flow.src.utils import prepare_environment_for_lean_dojo, repo_root

#command: /home/zhuxuekai/.elan/bin/lake
# args: [b'/home/zhuxuekai/.elan/bin/lake', b'env', b'lean', b'--threads=1', b'--memory=32768', b'Mathlib/Data/Relqk2dq38z.lean']
#

cached_path = os.path.expanduser(
    "/scratch2/nlp/zhuxuekai/reasoning_flow/baselines/.cache/lean_dojo/leanprover-community-mathlib4-29dcec074de168ac2bf835a77ef68bbe069194c5/mathlib4")
# repo = LeanGitRepo.from_path(cached_path)

build_deps = True
# cached_path = get_traced_repo_path(repo, build_deps)
# logger.info(f"Loading the traced repo from {cached_path}")
traced_repo = TracedRepo.load_from_disk(cached_path, build_deps)
traced_repo.check_sanity()

print("traced_files_graph", traced_repo.traced_files_graph)
print("traced_files", len(traced_repo.traced_files))

print("-----------------------")

traced_file = traced_repo.get_traced_file("Mathlib/Data/Relqk2dq38z.lean")
print(traced_file)
