LIST_CHECKSUM: str

def publicsuffix(
    domain: str,
    *,
    accept_unknown: bool = True,
    icann_only: bool = False,
    keep_case: bool = False,
) -> str | None:
    """Return the longest public suffix of *domain*, or None if it has none."""

def privatesuffix(
    domain: str,
    *,
    accept_unknown: bool = True,
    icann_only: bool = False,
    keep_case: bool = False,
) -> str | None:
    """
    Return the private suffix of *domain*: the public suffix plus one label.
    None if *domain* is entirely public, or invalid.
    """

def is_public(
    domain: str,
    *,
    accept_unknown: bool = True,
    icann_only: bool = False,
) -> bool:
    """Return whether *domain* is entirely a public suffix."""

def is_private(
    domain: str,
    *,
    accept_unknown: bool = True,
    icann_only: bool = False,
) -> bool:
    """Return whether *domain* is a private suffix or a subdomain of one."""

def privateparts(
    domain: str,
    *,
    accept_unknown: bool = True,
    icann_only: bool = False,
    keep_case: bool = False,
) -> tuple[str, ...] | None:
    """
    Return a tuple of the subdomain labels of *domain* followed by its private
    suffix, or None if it has no private suffix.
    """

def subdomain(
    domain: str,
    depth: int,
    *,
    accept_unknown: bool = True,
    icann_only: bool = False,
    keep_case: bool = False,
) -> str | None:
    """
    Return the suffix of *domain* reaching *depth* labels beyond its private
    suffix, or None if *domain* has too few labels. Depth 0 is the private
    suffix itself.
    """
