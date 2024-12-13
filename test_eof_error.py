from lean_dojo import *
from proof_flow.src.utils import prepare_environment_for_lean_dojo, repo_root

# def prepare_environment_for_lean_dojo():
#     # github access token
#     if not "GITHUB_ACCESS_TOKEN" in os.environ:
#         load_dotenv(get_config().paths.github_access_token)

#     # lean dojo cache path
#     cache_path_key = "CACHE_DIR"
#     if not cache_path_key in os.environ:
#         config_cache_path = get_config().paths.lean_dojo_cache_path
#         if config_cache_path is not None:
#             os.environ[cache_path_key] = config_cache_path

prepare_environment_for_lean_dojo()

#command: /home/zhuxuekai/.elan/bin/lake
# args: [b'/home/zhuxuekai/.elan/bin/lake', b'env', b'lean', b'--threads=1', b'--memory=32768', b'Mathlib/Data/Relqk2dq38z.lean']
#

cached_path = os.path.expanduser(
    "/scratch2/nlp/zhuxuekai/reasoning_flow/baselines/.cache/lean_dojo/leanprover-community-mathlib4-29dcec074de168ac2bf835a77ef68bbe069194c5/mathlib4")
# repo = LeanGitRepo.from_path(cached_path)

build_deps = True

traced_repo = TracedRepo.load_from_disk(cached_path, build_deps)
traced_repo.check_sanity()

print("traced_files_graph", traced_repo.traced_files_graph)
print("traced_files", len(traced_repo.traced_files))

print("-----------------------")

# traced_file = traced_repo.get_traced_file("Mathlib/Data/Relqk2dq38z.lean")
traced_file = traced_repo.get_traced_file("Mathlib/Algebra/ContinuedFractions/Translations2qx3rbck.lean")
print(traced_file)
