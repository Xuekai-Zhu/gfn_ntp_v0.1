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

repo = LeanGitRepo(
    "https://github.com/leanprover-community/mathlib4",
    "29dcec074de168ac2bf835a77ef68bbe069194c5",
)
traced_repo = trace(repo)

# traced_file = traced_repo.get_traced_file("Mathlib/Data/Relqk2dq38z.lean")
traced_file = traced_repo.get_traced_file("Mathlib/Algebra/ContinuedFractions/Translations2qx3rbck.lean")
print(traced_file)
