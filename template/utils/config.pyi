from typing import IO, Callable, Optional

from packaging.requirements import Requirement

from ._checks import check_type as check_type

def sys_info(fid: Optional[IO] = ..., developer: bool = ...):
    """Print the system information for debugging.

    Parameters
    ----------
    fid : file-like | None
        The file to write to, passed to :func:`print`. Can be None to use
        :data:`sys.stdout`.
    developer : bool
        If True, display information about optional dependencies.
    """

def _list_dependencies_info(
    out: Callable, ljust: int, package: str, dependencies: list[Requirement]
):
    """List dependencies names and versions."""
