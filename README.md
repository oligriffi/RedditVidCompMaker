# Reddit Video Downloader

Python script to download videos from Reddit and compiles them into one video.

## Requirements

* Python 3.6 or higher
* `requests`
* `objectpath`
* `json`
* `urllib`
* `moviepy`
* `pytube`

## Installation

1. Clone this repository.
2. Install the required packages using `pip`.
    ```
    pip install requests objectpath json urllib moviepy pytube
    ```
3. Run the script.
    ```
    python reddit_video_downloader.py
    ```

## Usage

This script downloads videos from the "tiktokcringe" subreddit on Reddit. To use it, you will need to fill in the following variables in the script:

* `CLIENT_ID`
* `SECRET_TOKEN`
* `USERNAME`
* `PASSWORD`

These variables are used to authenticate your Reddit account and generate an OAuth token, which is used to access the Reddit API.
