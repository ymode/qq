# qq
Quick Question - LLM in the terminal

<img src="https://github.com/user-attachments/assets/60dce499-561a-4ad0-b98a-67adaaf48e3a" width="300"/>


# Use
```qq how do I list files in terminal by size?```

<img width="983" alt="image" src="https://github.com/user-attachments/assets/ffe3490b-8429-4312-9771-1efeeb566534">



# Setup

💾 Manual Setup: install [dotenv](https://github.com/motdotla/dotenv) and [openai](https://github.com/openai/openai-python) on your system

🔑 Ensure your [OpenAI](https://openai.com/api/) API Key is exported in your .bashrc/.zshrc in the following format: ```export OPENAI_API_KEY=your openai key```

💻 Automatic Setup: In your Term, paste the following

```export OPENAI_API_KEY=your OpenAI API key
git clone https://github.com/ymode/qq.git
cd qq
pip install -r requirements.txt
chmod +x qq
sudo mv qq /usr/local/bin/
