# 3D_Object_Captioning
3D Vision-Language Agent: From Point Clouds to Natural Language

## 🎯Goal
### 🗂️Input
* 3D model files (`.ply`, `.obj`, `.pcd`), which will be converted into point cloud.

### 📝Output
* Description of objects in natural languages (captioning)
* Cross-references between text and 3D models.

## ✨Features
### 📤Upload 3D File
Users upload 3D files via a frontend API.

### 🛠️Pre-process Point Cloud
Standardize, sample, and normalize point cloud.

### 🎛️Extract 3D Feature
Extract high-dimensional feature vectors using PointNet++ / PointNetXt.

### 💬Generate Captions
A LLM pipeline converts 3D features into natural language descriptions.

### 🗃️Construct Embedding Index
Build a vector database using the 3D features or the generated caption embedding.

### 🔍Retrieval API
Enable users to search 3D models by captions, or search captions by 3D models.

### 🖼️Showcase Page
A page which renders the 3D models (enables 360-degree rotation views), together with the generated captions.

## ⚙️Requirements
* Inference time < 3s / model
* Program can be run on a Colab GPU instance.

## 🏗️System Design
```
┌───────────────┐
│ User Upload   │
│ 3D Model      │
└──────┬────────┘
       ↓
┌───────────────┐
│ Preprocessing │
│  - Sampling   │
│  - Normalizing│
└──────┬────────┘
       ↓
┌───────────────┐
│ PointNet++ /  │
│ PointNeXt     │
│ Feature Extract│
└──────┬────────┘
       ↓
┌───────────────┐
│ LLM Prompting │
│ Caption Gen   │
└──────┬────────┘
       ↓
┌───────────────┐
│ Vector DB     │
│ (FAISS)       │
└──────┬────────┘
       ↓
┌───────────────┐
│ Streamlit UI │
└───────────────┘

```

## 🛠️Used Libraries
* Read/Process Point Cloud: `open3d`
* Deep Learning: `torch`, `torchvision`, `torch-geometric`
* 3D models: `torch-point3d`, `torch-points-kernels`
* LLM APIs: `openai`, `google-generativeai`
* Vector Database: `faiss`, `chromadb`
* Front End: `gradio`, `streamlit`

## 📚Related Papers
* *PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space* [arXiv](https://arxiv.org/abs/1706.02413)
* *PointNeXt: Revisiting PointNet++ with Improved Training and Scaling Strategies (CVPR 2023)* [arXiv](https://arxiv.org/abs/2206.04670)
* *PaliGemma: A versatile 3B VLM for transfer* [arXiv](https://arxiv.org/abs/2407.07726)

## 📂Project Structure
```
.
├── data/                # 3D model examples
├── notebooks/           # Colab notebooks
├── scripts/
│   ├── preprocess.py    # Pre-process point cloud
│   ├── extract_feat.py  # 3D feature extraction
│   ├── caption.py       # Caption generation
│   └── retrieval.py     # Text-3D retrieval
├── app/                 # Streamlit frontend
├── requirements.txt
├── README.md
└── architecture.png     # System design
```