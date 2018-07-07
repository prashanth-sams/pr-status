

# Project description

Project contains a Python REST API written on flask which communicates with GitHub API and returns the current state of open PR's assuming the following workflow:

- REVIEWER_PENDING (PR created and reviewer is not assigned)
- REVIEW_IN_PROGRESS (Reviewer is assigned and PR is not yet approved)
- STATUS_CHECK_PENDING (PR is approved and status checks are not reported)
- FAILING (Status checks are failing for the PR)
- MERGE_PENDING (PR is approved and status checks have passed)

GET / endpoint returns the open PR states as json:

```json
{
  prs: [
    {
      "id": 1,
      "state": "REVIEWER_PENDING"
    },
    {
      "id": 2,
      "state": "FAILING"
    }
  ]
}
```

It assumes following environment variables:
- GITHUB_USERNAME
- GITHUB_PASSWORD
- GITHUB_REPO_OWNER
- GITHUB_REPO_NAME

Change these values in helm's values.yaml file and GITHUB_PASSWORD should be set in secrets.yaml inside templates folder. password should be base64 encoded.

# Monitoring
Project also exposes health metrics in prometheus format in GET /metrics. 

- request_latency_seconds_count
- request_latency_seconds_sum
- request_count
- Status codes of http requests

Prometheus's rate function allows calculation of both requests per second, and latency over time from this data.

# Packaging
The final solution includes Dockerfile as well as a helm chart for kubernetes deployment. The helm chart also pass linter checks and be written in accordance to helm's best practices.

Docker Image is already pushed to dockerhub repo staneja90. Image name and version can be found in helm values.yaml

# How to Run

helm install -n pr-status ./pr-status

# How to check

kubectl port-forward "pod" 5000:5000

go to http://localhost:5000/ for pr status and http://localhost:5000/metrics for prometheus exposed metrics

