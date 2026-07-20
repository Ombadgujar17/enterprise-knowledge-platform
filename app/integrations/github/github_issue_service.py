from app.config.logging import logger


class GitHubIssueService:
    """
    Service responsible for creating GitHub issues.
    """

    def create_issue(
        self,
        title: str,
        body: str,
    ) -> str:

        logger.info(
            "GitHub integration not configured."
        )

        raise NotImplementedError(
            "GitHub API integration has not been configured."
        )