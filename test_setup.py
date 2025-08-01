#!/usr/bin/env python3
"""
Test script to validate the LLM projects setup
This script tests if all required packages are installed and working correctly.
"""

import sys
import importlib
import warnings
warnings.filterwarnings('ignore')

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'transformers',
        'torch',
        'tensorflow',
        'openai',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'sklearn',
        'tiktoken',
        'dotenv',
        'tqdm',
        'tenacity',
        'datasets',
        'jupyter'
    ]
    
    print("🧪 Testing package imports...")
    failed_imports = []
    
    for package in required_packages:
        try:
            # Handle special cases
            if package == 'sklearn':
                importlib.import_module('sklearn')
            elif package == 'dotenv':
                importlib.import_module('dotenv')
            else:
                importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    return failed_imports

def test_transformers_basic():
    """Test basic transformers functionality"""
    print("\n🤖 Testing Transformers functionality...")
    try:
        from transformers import pipeline
        
        # Test sentiment analysis pipeline
        classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        result = classifier("This is a test message")
        
        if result and len(result) > 0 and 'label' in result[0]:
            print("✅ Sentiment analysis pipeline working")
            print(f"   Sample result: {result[0]['label']} ({result[0]['score']:.3f})")
            return True
        else:
            print("❌ Unexpected result format")
            return False
            
    except Exception as e:
        print(f"❌ Transformers test failed: {e}")
        return False

def test_data_processing():
    """Test basic data processing capabilities"""
    print("\n📊 Testing data processing...")
    try:
        import pandas as pd
        import numpy as np
        
        # Create sample data
        data = {
            'text': ['I love this!', 'This is okay', 'I hate this'],
            'label': ['positive', 'neutral', 'negative']
        }
        df = pd.DataFrame(data)
        
        # Basic operations
        assert len(df) == 3
        assert 'text' in df.columns
        assert df['text'].dtype == 'object'
        
        print("✅ Pandas operations working")
        
        # NumPy operations
        arr = np.array([1, 2, 3, 4, 5])
        assert arr.mean() == 3.0
        
        print("✅ NumPy operations working")
        return True
        
    except Exception as e:
        print(f"❌ Data processing test failed: {e}")
        return False

def test_visualization():
    """Test visualization capabilities"""
    print("\n📈 Testing visualization...")
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        import numpy as np
        
        # Test matplotlib
        fig, ax = plt.subplots(figsize=(6, 4))
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title("Test Plot")
        plt.close(fig)  # Don't display, just test
        
        print("✅ Matplotlib working")
        
        # Test seaborn
        sns.set_style("whitegrid")
        print("✅ Seaborn working")
        
        return True
        
    except Exception as e:
        print(f"❌ Visualization test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Starting LLM Projects Setup Test")
    print("=" * 50)
    
    # Test imports
    failed_imports = test_imports()
    
    if failed_imports:
        print(f"\n❌ Failed imports: {', '.join(failed_imports)}")
        print("Please install missing packages with:")
        print(f"pip install {' '.join(failed_imports)}")
        return False
    
    # Test functionality
    tests = [
        test_transformers_basic,
        test_data_processing,
        test_visualization
    ]
    
    passed_tests = 0
    for test in tests:
        try:
            if test():
                passed_tests += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed_tests}/{len(tests) + 1} tests passed")
    
    if passed_tests == len(tests) and not failed_imports:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Open 'Exploring NLP through Hugging Face Transformers Library.ipynb'")
        print("2. Open 'Empathy_Chatbot_Improved.ipynb' for the fine-tuning project")
        print("3. Set up your OpenAI API key in environment variables if needed")
        return True
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)