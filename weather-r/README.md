# Weather

## Requirements

- `R`

### Installing R in Manjaro

```bash
sudo pacman -S r
```

### Config install

```bash
mkdir -p ~/R/x86_64-pc-linux-gnu-library
```

```bash
# ~/.Rprofile
.libPaths("~/R/x86_64-pc-linux-gnu-library/")
options(repos = c(CRAN = "https://cran.rstudio.com/"))
```

## Scripts

```bash
cd scripts
```
