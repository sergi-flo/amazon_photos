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
## Command to execute 

You can execute the command giving it executions permission as the following:

```bash
./amazon_photos.py source_dir destination_dir
```

or with the python comand as follows:

```bash
pyhton3 amazon_photos.py source_dir destination_dir
```

You also can get help as what the command does, and the args it need with the command:

```bash
pyhton3 amazon_photos.py -h

or 

./amazon_photos.py -h
```

