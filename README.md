# Local Dub Auto

Fully automatic Hindi -> English (or any supported pair) video dubbing.

## How it works
1. Drop videos into the Google Drive folder **DubInbox** (any number).
2. Every **20 minutes** GitHub Actions wakes up and dubs **all** of them,
   oldest first. Empty inbox = the run exits in seconds.
3. Dubbed videos land in **DubDone**; originals move to **DubInbox/archive**.

Manual runs (Actions tab -> "Auto Dub from Drive" -> Run workflow) let you
override language, genre, chunk size, etc.

## YouTube links (yt-dlp)
Drop a `.txt` file in DubInbox with one YouTube URL per line - each link is
downloaded on its own runner and dubbed. Or use the manual run's `url` input.

## Setup
Add repo secret **RCLONE_CONF** = your rclone Google Drive config text.

## Notes
- One run processes the whole queue (up to ~5h of work; leftovers roll over).
- Failed chunks ship next to the video in `*_FAILED_CHUNKS` with a README.
- GitHub pauses cron schedules after ~60 days with no repo activity; any
  commit re-enables them.

