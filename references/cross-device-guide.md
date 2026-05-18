# Cross-Device Guide

Use this reference when work spans laptops, lab machines, servers, cloud instances, deployment targets, or removable storage.

## Device Record Fields

| Field | Meaning |
| --- | --- |
| Device alias | Short stable name, such as `local-laptop`, `lab-4090`, `train-server`, or `prod-vm`. |
| Role | Editing, training, evaluation, deployment, data storage, visualization, or backup. |
| Hardware | CPU/GPU/RAM details when relevant. |
| OS / runtime | Operating system, CUDA, Python, Node, Docker, Conda, or package manager. |
| Project path | Root path on that device. |
| Data paths | Dataset, cache, checkpoint, output, and log locations. |
| Sync status | What has been copied, committed, pushed, pulled, or still missing. |
| Unknowns | Items that must be confirmed before running commands. |

## Cross-Device Handoff Pattern

When a task must continue on another machine, record:

1. Current device and target device.
2. Files changed locally.
3. Git branch and commit or uncommitted change state.
4. Artifacts that exist outside Git.
5. Data or checkpoints required on the target machine.
6. Exact command to run next.
7. Expected output path and validation criteria.
8. Items the future agent must confirm before execution.

## Recommended Device Aliases

Use stable aliases rather than one-off descriptions:

- `local-laptop`
- `lab-workstation`
- `training-server`
- `deployment-server`
- `cloud-runner`
- `external-storage`

If the user provides a preferred alias, keep using it.
