# CV source

The PDFs in `cv/` are generated from `build_cv.py`.

1. Edit the text in `build_cv.py` (`CONTENT["en"]` and `CONTENT["sv"]`).
2. From the repository root run:

```
python3 cv/source/build_cv.py
node cv/source/render_pdf.js
```

`render_pdf.js` needs Node with Playwright and Chromium installed. `photo.jpg` is the CV photo.
