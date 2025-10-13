## 支持的语言
[![Русский](https://img.shields.io/badge/lang-Русский-blue)](README.md)
[![中文](https://img.shields.io/badge/lang-中文-green)](docs/README.zh.md)
[![English](https://img.shields.io/badge/lang-English-green)](docs/README.en.md)

**运行本项目需要安装 git、Docker 和 curl**

## 脚本说明
从项目根目录通过 Bash 运行（例如：`bash start.sh`；在 Windows 上可直接双击 `.bat` 文件）：
- `start.sh` / `.bat` — 启动应用并构建镜像  
- `stop.sh` / `.bat` — 停止应用容器（不删除镜像）  
- `remove.sh` / `.bat` — 停止正在运行的容器（如有），并删除镜像以释放存储空间  
- `rebuild.sh` / `.bat` — 从 Git 拉取最新版本代码，重新构建镜像并启动容器  

## 使用方法（在运行 `start.sh`/`.bat` 或 `rebuild.sh`/`.bat` 之后）
- **UI 版本**：在浏览器地址栏输入 `http://localhost:8501` 即可访问  
- **CLI 版本**：在命令行中执行以下命令：
  ```bash
  curl -X 'POST' \
    'http://localhost:2307/run_cli' \
    -F 'file=@path/to/file' \
    -F 'particle_type=he|p' \
    -F 'model_type=mlp|cnn'
  ```
  也可在浏览器中打开 `http://localhost:2307/docs` 手动上传文件。

***处理结果将保存在 `storage` 文件夹中，文件名和格式与原始文件相同，但会额外包含字段 `p|he_bin_$bin_number`。***

## 数据集格式
- **未来模型所需字段**：  
  `date`, `BRBG`, `MRNY`, `SOPO`, `THUL`, `TXBY`, `APTY`, `OULU`, `KERG`, `YKTK`, `MOSC`, `NVBK`, `LMKS`, `JUNG`, `AATB`, `MXCO`, `ATHN`, `PSNM`, `Ap`, `SSN`, `A`

- **历史模型所需字段**：  
  `date`, `BRBG`, `THUL`, `TXBY`, `APTY`, `OULU`, `KERG`, `YKTK`, `MOSC`, `NVBK`, `LMKS`, `JUNG`, `AATB`, `MXCO`, `ATHN`, `Ap`, `SSN`, `A`