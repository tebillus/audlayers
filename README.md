to run this you should get uv (astral.sh/uv) (cos uv's good)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

when you get the project cloned, add a .mp3 or an .wav file,
then do the following,;

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

[here it is in action;](https://www.youtube.com/watch?v=ewg8u7_UoQY)
