# My LLM Learning Journey

This repository documents my learning journey through Large Language Models (LLMs), from basic NLP tasks to advanced fine-tuning techniques.

## What I'm Learning

### 1. NLP with Hugging Face Transformers
**File:** `Exploring NLP through Hugging Face Transformers Library.ipynb`

My exploration of various NLP tasks:
- **Sentiment Analysis**: Learning to use DistilBERT for emotion detection
- **Emotion Recognition**: Working with RoBERTa for advanced emotion classification
- **Text Summarization**: Experimenting with automated text summarization
- **Language Translation**: Testing multi-language translation capabilities
- **Text Generation**: Trying creative text generation with GPT-2
- **Named Entity Recognition**: Extracting entities from text
- **Question Answering**: Building context-based question answering systems
- **Fill-Mask**: Exploring text completion and mask filling

**What I've implemented:**
- Interactive visualizations and analysis
- Error handling and edge case testing
- Batch processing capabilities
- Performance metrics and evaluation

### 2. Empathy Chatbot with GPT-3.5 Fine-tuning
**Files:** 
- `Empathy_Chatbot_Improved.ipynb` (My enhanced version)
- `Prompt_engineering.ipynb` (My initial attempt)

My deep dive into fine-tuning:
- **Secure API Management**: Learning environment-based API key handling
- **Data Processing**: Cleaning and preparing empathetic dialogues dataset
- **Cost Estimation**: Understanding fine-tuning costs before training
- **Training Monitoring**: Implementing real-time progress tracking
- **Model Evaluation**: Building comprehensive testing frameworks
- **Production Ready**: Adding error handling, logging, and retry logic

**Dataset:** Empathetic Dialogues (Facebook AI Research)
**Model:** GPT-3.5-turbo fine-tuning for empathetic responses

## How to Run My Projects

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
For my GPT-3.5 fine-tuning project, set up your OpenAI API key:

```bash
# Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Or set environment variable:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

## How I Use These Projects

### Running My NLP Transformers Notebook
1. Launch Jupyter: `jupyter notebook`
2. Open `Exploring NLP through Hugging Face Transformers Library.ipynb`
3. Run cells sequentially to explore different NLP tasks

### Running My Empathy Chatbot Project
1. Open `Empathy_Chatbot_Improved.ipynb`
2. Follow the security guidelines for API key setup
3. Review cost estimates before starting fine-tuning
4. Monitor training progress and evaluate results

## Security Best Practices I Follow

- Never commit API keys to version control
- Use environment variables for sensitive data
- Validate inputs and handle errors gracefully
- Monitor costs and usage limits
- Follow OpenAI's usage policies

## My Project Structure

```
LLMs/
├── README.md                                          # This file
├── requirements.txt                                   # Python dependencies
├── test_setup.py                                     # Setup validation script
├── Exploring NLP through Hugging Face Transformers Library.ipynb  # My NLP experiments
├── Empathy_Chatbot_Improved.ipynb                   # My enhanced chatbot project
└── Prompt_engineering.ipynb                         # My initial chatbot attempt
```

## My Learning Progress

### Beginner Level - Completed
- Understanding transformer architectures
- Using pre-trained models for various NLP tasks
- Data preprocessing and visualization
- Basic prompt engineering techniques

### Intermediate Level - In Progress
- Fine-tuning pre-trained models
- Custom dataset preparation
- Model evaluation and metrics
- Cost optimization for training

### Advanced Level - Future Goals
- Production-ready code architecture
- Error handling and monitoring
- Security best practices
- Scalable deployment considerations

## What I've Improved Over Time

### Code Quality
- **Modular Design**: Learned object-oriented programming with clear separation of concerns
- **Error Handling**: Added comprehensive exception handling and logging
- **Type Hints**: Enhanced code readability and IDE support
- **Documentation**: Added detailed docstrings and comments

### Performance
- **Batch Processing**: Implemented efficient handling of multiple inputs
- **Memory Management**: Optimized data loading and processing
- **Progress Tracking**: Added real-time monitoring with progress bars

### Security
- **API Key Management**: Learned secure handling of sensitive credentials
- **Input Validation**: Added sanitization and validation of user inputs
- **Cost Control**: Implemented estimation and monitoring of API usage costs

### User Experience
- **Interactive Testing**: Built real-time model interaction
- **Visualization**: Created rich charts and graphs for data analysis
- **Clear Feedback**: Added informative success and error messages

## What I Plan to Learn Next

1. **Expand Model Coverage**: Experiment with more transformer variants (BERT, T5, etc.)
2. **Custom Training**: Learn training from scratch techniques
3. **Deployment**: Explore containerization and cloud deployment
4. **Evaluation Metrics**: Study advanced model evaluation techniques
5. **Advanced Techniques**: Dive into RAG, agents, and tool calling

## Contributing

Feel free to contribute by:
- Adding new NLP tasks and models
- Improving documentation and tutorials
- Reporting bugs and suggesting enhancements
- Sharing your own LLM experiments

## License

This project is for educational purposes. Please respect the licenses of the underlying models and datasets used.

---

**Happy Learning!**
