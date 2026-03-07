# Fonts Directory

This directory contains local fonts for Typst projects.

## Usage

### List Available Fonts
```bash
python3 scripts/manage_fonts.py list
```

### Check Font Availability
```bash
python3 scripts/manage_fonts.py check "Libertinus Serif"
```

### Install a Font
```bash
python3 scripts/manage_fonts.py install /path/to/font.ttf
```

## Supported Formats
- `.ttf` - TrueType Font
- `.otf` - OpenType Font
- `.woff` - Web Open Font Format
- `.woff2` - Web Open Font Format 2

## Recommended Fonts for Typst

| Font | Use Case | License |
|------|----------|---------|
| Libertinus Serif | Body text | OFL |
| Libertinus Sans | Headings | OFL |
| Fira Code | Code blocks | OFL |
| Source Code Pro | Code blocks | OFL |
| New Computer Modern | Math | OFL |

## Font Installation Locations

Typst searches for fonts in:
1. System font directories
2. `TYPST_FONT_PATHS` environment variable
3. Local project directories

## Adding Fonts to This Directory

1. Download font files (ensure permissive license)
2. Copy `.ttf` or `.otf` files here
3. Run `typst fonts` to verify detection

## License Compliance

Only use fonts with permissive licenses:
- SIL Open Font License (OFL)
- Apache 2.0
- MIT
- Public Domain

Verify license before adding any font.
