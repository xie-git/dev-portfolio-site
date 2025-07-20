# Portfolio Media Assets

## Directory Structure

```
static/
├── images/
│   ├── projects/           # Project screenshots and images
│   │   ├── chicago_analytics.png
│   │   ├── aigeneratedai.png
│   │   └── homelab_image.png
│   ├── companies/          # Company logos (small versions for timeline)
│   │   ├── northern_trust_small.png
│   │   ├── capital_one_small.png
│   │   ├── northwestern_mutual_small.png
│   │   ├── northern_trust_large.png
│   │   ├── capital_one_large.png
│   │   └── northwestern_mutual_large.png
│   ├── profile/            # Profile and personal images
│   ├── icons/              # Icons and small graphics
│   └── portfolio/          # Portfolio showcase images
├── fonts/                  # Custom fonts
├── css/                    # Additional stylesheets (if needed)
└── js/                     # Additional JavaScript files (if needed)
```

## Usage

### Project Images
- Used in project panels and modals
- Referenced in `simple_app.py` projects array as `placeholder` field
- Path format: `/static/images/projects/filename.png`

### Company Logos
- `*_small.png`: Used in timeline entries (24x24px optimal)
- `*_large.png`: Reserved for larger displays or detailed views
- Path format: `/static/images/companies/company_name_size.png`

## Adding New Assets

1. **Project Images**: Add to `static/images/projects/`
2. **Company Logos**: Add both small and large versions to `static/images/companies/`
3. **Update Code**: Modify the relevant project or timeline entry in `simple_app.py`

## Logo Guidelines

- **Small logos**: 24x24px, optimized for timeline display
- **Large logos**: 48x48px or larger for detailed views
- **Format**: PNG with transparent background preferred
- **Naming**: `company_name_size.png` (e.g., `northern_trust_small.png`) 