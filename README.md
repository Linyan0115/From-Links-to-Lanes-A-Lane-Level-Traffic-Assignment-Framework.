# From Links to Lanes: A Lane-Level Traffic Assignment Framework

This repository accompanies the research project “From Links to Lanes: A Lane-Level Traffic Assignment Framework”, presented at the 2025 INFORMS Annual Meeting.

It includes the methodological description, simulation tools, figures used in the presentation, and replication instructions for running lane-level dynamic traffic assignment (DTA) experiments and microscopic SUMO simulations.

## Overview

Traditional link-based traffic assignment (DTA) models treat each road segment as a single homogeneous link and fail to represent:

- lane-changing friction

- turning-pocket spillback

- cross-weave turbulence

- lane-level capacity constraints

Modern transportation networks—especially with connected vehicles, HD maps, and autonomous driving—require lane-level fidelity.

This project develops a Lane-Level Dynamic Traffic Assignment (DTA) framework that models:

- Straight movements

- Turning movements

- Lane-changing maneuvers

via maneuver-specific volume–delay functions (VDFs) that depend on traffic flow in both origin and receiving lanes.

The model is validated against microscopic SUMO simulations and real-world Sioux Falls experiments.

## Informs Meeting Slides

<img width="811" height="454" alt="Screenshot 2025-11-29 at 4 11 51 AM" src="https://github.com/user-attachments/assets/a99f335c-a5cd-46a4-bdc3-363da1a68fcf" />
<img width="810" height="449" alt="Screenshot 2025-11-29 at 4 12 24 AM" src="https://github.com/user-attachments/assets/382003be-8d5c-48a8-9a8f-6294828c5eb8" />
<img width="808" height="451" alt="Screenshot 2025-11-29 at 4 12 43 AM" src="https://github.com/user-attachments/assets/cda4ff70-d8d0-4242-ad51-e1d99552bd79" />
<img width="807" height="451" alt="Screenshot 2025-11-29 at 4 12 57 AM" src="https://github.com/user-attachments/assets/9e053cd9-a3af-4861-a67b-958eb5d0ae0f" />
<img width="809" height="453" alt="Screenshot 2025-11-29 at 4 13 09 AM" src="https://github.com/user-attachments/assets/c3aa2d86-8758-4637-b8da-be4a4b2b494d" />
<img width="811" height="459" alt="Screenshot 2025-11-29 at 4 13 22 AM" src="https://github.com/user-attachments/assets/4624797b-4c7c-4fdf-8543-6e790c4b369e" />
<img width="809" height="456" alt="Screenshot 2025-11-29 at 4 13 34 AM" src="https://github.com/user-attachments/assets/1636e0f3-fb09-4acc-a951-961810f453a4" />
<img width="813" height="456" alt="Screenshot 2025-11-29 at 4 13 47 AM" src="https://github.com/user-attachments/assets/bf8b7e4c-2bec-4688-9157-d74657a65629" />
<img width="812" height="457" alt="Screenshot 2025-11-29 at 4 13 59 AM" src="https://github.com/user-attachments/assets/34c73037-ce29-4357-bfaa-c5015cb348e9" />

## Abstract Paper
[Click to view the Abstract Paper](paper/Abstract%20Paper.pdf)











