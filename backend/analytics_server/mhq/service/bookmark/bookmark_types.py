from enum import Enum


class BookmarkType(Enum):

    ORG_REPO_BOOKMARK = "ORG_REPO_BOOKMARK"
    INCIDENT_SERVICE_BOOKMARK = "INCIDENT_SERVICE_BOOKMARK"
    REPO_WORKFLOW_BOOKMARK = "REPO_WORKFLOW_BOOKMARK"
    MERGE_TO_DEPLOY_BOOKMARK = "MERGE_TO_DEPLOY_BOOKMARK"
