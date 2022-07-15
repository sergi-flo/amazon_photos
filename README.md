# Amazon Photos script

Automated script to separate phto files from video files into 2 separate folders, but without deordering the folder structure the folder had. This script was created for storing all the photon in amazon cloud, as it offered free unlimited storage but just for photos.

Example of how this script would work:

**Before script:**
folder_photos_videos
\__Summer_2020
    \__July
    \__August
\__Ski_2021
    \__Alps
    \__Party

**After Script:**
folder_photos_videos_separated
\__photos (Just contains photos files)
    \__Summer_2020
        \__July
        \__August
    \__Ski_2021
        \__Alps
        \__Party
\__video (Just contains video files)
    \__Summer_2020
        \__July
        \__August
    \__Ski_2021
        \__Alps
        \__Party

