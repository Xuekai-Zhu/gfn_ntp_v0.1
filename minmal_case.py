from lean_dojo import *


# my local cache : lean_dojo/leanprover-community-mathlib4-29dcec074de168ac2bf835a77ef68bbe069194c5/mathlib4
# also equal to : 
# repo = LeanGitRepo(
#     "https://github.com/leanprover-community/mathlib4",
#     "29dcec074de168ac2bf835a77ef68bbe069194c5",
# )
# traced_repo = trace(repo)

cached_path = os.path.expanduser(
    "/scratch2/nlp/zhuxuekai/reasoning_flow/baselines/.cache/lean_dojo/leanprover-community-mathlib4-29dcec074de168ac2bf835a77ef68bbe069194c5/mathlib4")

build_deps = True
traced_repo = TracedRepo.load_from_disk(cached_path, build_deps)
# traced_repo.check_sanity()

traced_file = traced_repo.get_traced_file("Mathlib/Algebra/ContinuedFractions/Translations2qx3rbck.lean")
print(traced_file)