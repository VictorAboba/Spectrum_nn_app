## Available Languages
[![Русский](https://img.shields.io/badge/lang- Русский-blue)](README.md)
[![中文](https://img.shields.io/badge/lang- 中文-green?logo=github)](README.zh.md)
[![English](https://img.shields.io/badge/lang-English-green)](docs/README.en.md)

**Git, Docker, and curl are required to run this project.**

## Scripts
Run from the project root using Bash (e.g., `bash start.sh`; on Windows, simply double-click the `.bat` file):
- `start.sh` / `.bat` — starts the application and builds the image  
- `stop.sh` / `.bat` — stops the application container without removing the image  
- `remove.sh` / `.bat` — stops the container (if running) and removes the image, freeing up disk space  
- `rebuild.sh` / `.bat` — pulls the latest version of the application from Git, rebuilds the image, and starts the container  

## Usage (after running `start.sh`/`.bat` or `rebuild.sh`/`.bat`)
- **UI version** — open your browser and navigate to `http://localhost:8501`  
- **CLI version** — run the following command in your terminal:  
  ```bash
  curl -X 'POST' \
    'http://localhost:2307/run_cli' \
    -F 'file=@path/to/file' \
    -F 'particle_type=he|p' \
    -F 'model_type=mlp|cnn'
  ```
  You can also manually upload a file via your browser at `http://localhost:2307/docs`.

***The processed output will be saved in the `storage` folder with the same filename and format as the original, but with additional fields: `p|he_bin_$bin_number`.***

## Dataset Format
- **Fields required for future models**:  
  `date`, `BRBG`, `MRNY`, `SOPO`, `THUL`, `TXBY`, `APTY`, `OULU`, `KERG`, `YKTK`, `MOSC`, `NVBK`, `LMKS`, `JUNG`, `AATB`, `MXCO`, `ATHN`, `PSNM`, `Ap`, `SSN`, `A`

- **Fields required for historical models**:  
  `date`, `BRBG`, `THUL`, `TXBY`, `APTY`, `OULU`, `KERG`, `YKTK`, `MOSC`, `NVBK`, `LMKS`, `JUNG`, `AATB`, `MXCO`, `ATHN`, `Ap`, `SSN`, `A`