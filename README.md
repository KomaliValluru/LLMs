# Learning Repository for Large Language Models (LLMs)

This repository contains comprehensive projects and tutorials for learning and implementing various LLM techniques, from basic NLP to advanced fine-tuning.

## 🚀 Projects Overview

### 1. NLP with Hugging Face Transformers
**File:** `Exploring NLP through Hugging Face Transformers Library.ipynb`

- ✅ **Sentiment Analysis**: Using DistilBERT for emotion detection
- ✅ **Emotion Recognition**: Advanced emotion classification with RoBERTa
- ✅ **Text Summarization**: Automated text summarization
- ✅ **Language Translation**: Multi-language translation capabilities
- ✅ **Text Generation**: Creative text generation with GPT-2
- ✅ **Named Entity Recognition**: Extract entities from text
- ✅ **Question Answering**: Context-based question answering
- ✅ **Fill-Mask**: Text completion and mask filling

**Features:**
- Interactive visualizations and analysis
- Error handling and edge case testing
- Batch processing capabilities
- Performance metrics and evaluation

### 2. Empathy Chatbot with GPT-3.5 Fine-tuning
**Files:** 
- `Empathy_Chatbot_Improved.ipynb` (Enhanced version)
- `Prompt_engineering.ipynb` (Original version)

- ✅ **Secure API Management**: Environment-based API key handling
- ✅ **Data Processing**: Clean and prepare empathetic dialogues dataset
- ✅ **Cost Estimation**: Calculate fine-tuning costs before training
- ✅ **Training Monitoring**: Real-time progress tracking
- ✅ **Model Evaluation**: Comprehensive testing framework
- ✅ **Production Ready**: Error handling, logging, and retry logic

**Dataset:** Empathetic Dialogues (Facebook AI Research)
**Model:** GPT-3.5-turbo fine-tuning for empathetic responses

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd LLMs
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Validate Setup
```bash
python test_setup.py
```

### 4. Environment Setup (Optional)
For the GPT-3.5 fine-tuning project, set up your OpenAI API key:

```bash
# Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Or set environment variable:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

## 📚 Usage

### Running the NLP Transformers Notebook
1. Launch Jupyter: `jupyter notebook`
2. Open `Exploring NLP through Hugging Face Transformers Library.ipynb`
3. Run cells sequentially to explore different NLP tasks

### Running the Empathy Chatbot Project
1. Open `Empathy_Chatbot_Improved.ipynb`
2. Follow the security guidelines for API key setup
3. Review cost estimates before starting fine-tuning
4. Monitor training progress and evaluate results

## 🔒 Security Best Practices

- ✅ Never commit API keys to version control
- ✅ Use environment variables for sensitive data
- ✅ Validate inputs and handle errors gracefully
- ✅ Monitor costs and usage limits
- ✅ Follow OpenAI's usage policies

## 📊 Project Structure

```
LLMs/
├── README.md                                          # This file
├── requirements.txt                                   # Python dependencies
├── test_setup.py                                     # Setup validation script
├── Exploring NLP through Hugging Face Transformers Library.ipynb  # NLP tutorial
├── Empathy_Chatbot_Improved.ipynb                   # Enhanced chatbot project
└── Prompt_engineering.ipynb                         # Original chatbot (legacy)
```

## 🎯 Learning Objectives

### Beginner Level
- [x] Understanding transformer architectures
- [x] Using pre-trained models for various NLP tasks
- [x] Data preprocessing and visualization
- [x] Basic prompt engineering techniques

### Intermediate Level
- [x] Fine-tuning pre-trained models
- [x] Custom dataset preparation
- [x] Model evaluation and metrics
- [x] Cost optimization for training

### Advanced Level
- [x] Production-ready code architecture
- [x] Error handling and monitoring
- [x] Security best practices
- [x] Scalable deployment considerations

## 🔧 Technical Improvements Made

### Code Quality
- ✅ **Modular Design**: Object-oriented programming with clear separation of concerns
- ✅ **Error Handling**: Comprehensive exception handling and logging
- ✅ **Type Hints**: Enhanced code readability and IDE support
- ✅ **Documentation**: Detailed docstrings and comments

### Performance
- ✅ **Batch Processing**: Efficient handling of multiple inputs
- ✅ **Memory Management**: Optimized data loading and processing
- ✅ **Progress Tracking**: Real-time monitoring with progress bars

### Security
- ✅ **API Key Management**: Secure handling of sensitive credentials
- ✅ **Input Validation**: Sanitization and validation of user inputs
- ✅ **Cost Control**: Estimation and monitoring of API usage costs

### User Experience
- ✅ **Interactive Testing**: Real-time model interaction
- ✅ **Visualization**: Rich charts and graphs for data analysis
- ✅ **Clear Feedback**: Informative success and error messages

## 📈 Next Steps

1. **Expand Model Coverage**: Add more transformer variants (BERT, T5, etc.)
2. **Custom Training**: Implement training from scratch tutorials
3. **Deployment**: Add containerization and cloud deployment guides
4. **Evaluation Metrics**: Expand model evaluation techniques
5. **Advanced Techniques**: Include RAG, agents, and tool calling

## 🤝 Contributing

Feel free to contribute by:
- Adding new NLP tasks and models
- Improving documentation and tutorials
- Reporting bugs and suggesting enhancements
- Sharing your own LLM experiments

## 📄 License

This project is for educational purposes. Please respect the licenses of the underlying models and datasets used.

---

**Happy Learning! 🚀🤖**
