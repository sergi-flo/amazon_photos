# Amazon Photos script

Automated script to separate phto files from video files into 2 separate folders, but without deordering the folder structure the folder had. This script was created for storing all the photon in amazon cloud, as it offered free unlimited storage but just for photos.

Example of how this script would work:
```bash
Before script:
folder_photos_videos
├── Summer_2020
│   ├── July
│   └── August  
└── Ski_2021
    ├── Alps
    └── Spain 

After Script:
folder_photos_videos_separated
├── photos (Just contains photos files)
│   ├── Summer_2020
│   │   ├── July
│   │   └── August  
│   └── Ski_2021
│       ├── Alps
│       └── Spain   
└── videos (Just contains video files)
    ├── Summer_2020
    │   ├── July
    │   └── August  
    └── Ski_2021
        ├── Alps
        └── Spain  
```
