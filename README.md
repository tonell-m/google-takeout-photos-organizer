# Google takeout organizer

A utility tool to organize photos and videos downloaded via takeout.google.com.

When you download your photos using Google Takeout, all creation and modiciation dates will be equal to the current datetime.
Since the archive also contains a metadata file for each element with the original date and time, we can use those metadata
to restore the original metadata of the pictures, then delete the JSON files to cleanup the directory.


# Usage

Create and activate python virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
```

Run tool:

```sh
python -m sortpics {/Path/To/Root/Directory}
```

Voilà!
