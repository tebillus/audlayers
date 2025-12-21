haaaaaaaaaaaaaaaaaaaaaaaa

oh yea there are things i should add here

to run this you should get uv (astral.sh/uv) (cos uv's good)

```bash
uv venv
source .venv/bin/activate
uv pip install opencv-python ultralytics pygame
uv run audlayers.py
```

to snipe everything and clear up storage when you're done, do the following:

```bash
uv pip uninstall opencv-python ultralytics pygame
deactivate
rm -rf .venv
```

good day to you!
